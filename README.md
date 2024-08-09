# Processamento de Dados de Cartão de Crédito e Extrato Conta C6

Este repositório contém um script Python para processar dados de extrato de cartão de crédito a partir de um arquivo CSV e exportá-los para um arquivo XLSX. O script realiza diversas operações, incluindo a filtragem de dados, renomeação de colunas, e formatação de datas.

* c6_csv_to_xlsx.py: Converte uma fatura C6 Cartão de Crédito CSV para o formato XLSX para ser utilizado como arquivo de importação para o gerenciador financeiro **Mobills**;

* [pdf_parser.py](https://github.com/djkakaroto/C6-bank-automation): Converte o extrato da Conta C6 em PDF para CSV para ser importado pelo **Mobills**;

## Funcionalidades

1. **Leitura do CSV**: Lê um arquivo CSV com dados do extrato de cartão de crédito usando delimitador ponto e vírgula (`;`).
2. **Filtragem de Dados**: Remove linhas onde a coluna `Descrição` contém a string `"Inclusao de Pagamento"`.
3. **Conversão de Data**: Converte a coluna `Data de Compra` para o formato de data.
4. **Renomeação de Coluna**: Renomeia a coluna `Valor (em R$)` para `Valor`.
5. **Combinação de Colunas**: Cria uma nova coluna `Descrição` combinando `Descrição` e `Parcela`, deixando `Parcela` em branco se `Parcela` for `"Única"`.
6. **Adição de Coluna**: Adiciona uma nova coluna `Conta` em branco após a coluna `Valor`.
7. **Reordenação das Colunas**: Reordena as colunas conforme solicitado.
8. **Exportação para XLSX**: Salva o DataFrame processado em um arquivo XLSX.
9. **Formatação de Data**: Aplica formatação à coluna de data no arquivo XLSX.

## Requisitos

- Python 3.x
- Pandas
- OpenPyXL

Você pode instalar as dependências necessárias usando pip:

```sh
pip install pandas openpyxl
```

## Uso

1. Configurar os Caminhos dos Arquivos:

Edite o script para definir os caminhos dos arquivos CSV e XLSX.

```python
caminho_arquivo_csv = 'caminho/para/seu/arquivo.csv'
caminho_arquivo_xlsx = 'caminho/para/seu/arquivo.xlsx'
```

2. Executar o Script:

Execute o script Python para processar os dados e gerar o arquivo XLSX.

```sh
python seu_script.py
```

3. Verificar o Arquivo XLSX:

O arquivo XLSX será salvo no caminho especificado. Verifique o arquivo para garantir que os dados foram processados e formatados conforme esperado.

# Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, crie um fork do repositório, faça suas alterações e envie um pull request.

# Licença
Este projeto está licenciado sob a Licença MIT.