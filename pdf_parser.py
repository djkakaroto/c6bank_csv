import os
import time
import csv
from PyPDF2 import PdfReader
from datetime import datetime


def parse_pdf(file_path, output_csv):
    transactions = []

    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split("\n")

            for line in lines:
                parts = line.split(" ")

                if len(parts) >= 5:
                    date_str = parts[0]
                    description = " ".join(parts[1:-2])
                    amount = parts[-2]
                    transaction_type = parts[-1]

                    try:
                        # date = datetime.strptime(date_str, '%d/%m/%Y')
                        date = date_str

                        # Ignorar linhas com descrições contendo "SALDO" ou "TOTAL DISPONÍVEL PARA SAQUE"
                        if not (
                            description.startswith(" -    ")
                            or "SALDO" in description
                            or "TOTAL DISPONÍVEL PARA SAQUE" in description
                        ):
                            # Remover "000000000000" da descrição
                            description = description.replace(
                                "000000000000", ""
                            ).strip()
                            # Substituir "-" por " - "
                            description = description.replace("-", " - ")

                            if transaction_type == "D":
                                amount = "-" + amount

                            transactions.append(
                                [
                                    date,
                                    description,
                                    amount,
                                    "Carteira",
                                    "Categoria",
                                    transaction_type,
                                ]
                            )
                    except ValueError:
                        # Ignorar linhas com data inválida
                        pass
    # Escrever as transações em um arquivo CSV
    with open(output_csv, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["Data", "Descrição", "Valor", "Conta", "Tipo de Transação"]
        )
        csv_writer.writerows(transactions)

    return transactions


def parse_c6_cartao_pdf(file_path, output_csv):
    transactions = []

    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split("\n")

            for line in lines:
                parts = line.split(" ")

                if len(parts) >= 5:
                    date_str = parts[0]
                    # print(date_str)
                    # time.sleep(20)
                    description = " ".join(parts[2:-1])
                    amount = parts[-1]
                    # transaction_type = parts[-3]

                    try:
                        # date = datetime.strptime(date_str, '%d/%m/%Y')
                        date = f"{date_str}"

                        # Ignorar linhas com descrições contendo "SALDO" ou "TOTAL DISPONÍVEL PARA SAQUE"
                        if not (
                            description.startswith(" -    ")
                            or "SALDO" in description
                            or "TOTAL DISPONÍVEL PARA SAQUE" in description
                        ):
                            # Remover "000000000000" da descrição
                            description = description.replace(
                                "000000000000", ""
                            ).strip()
                            # Substituir "-" por " - "
                            description = description.replace("-", " - ")

                            transactions.append(
                                [date, description, amount, "Carteira", "Categoria"]
                            )
                    except ValueError:
                        # Ignorar linhas com data inválida
                        pass
    # Escrever as transações em um arquivo CSV
    with open(output_csv, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["Data", "Descrição", "Valor", "Conta", "Tipo de Transação"]
        )
        csv_writer.writerows(transactions)

    return transactions


pdf_path = "caminho_do_extrato.pdf"
output_csv = "transacoes_c6.csv"
transactions = parse_c6_cartao_pdf(pdf_path, output_csv)
print(f"Transações extraídas e gravadas em {output_csv}")
