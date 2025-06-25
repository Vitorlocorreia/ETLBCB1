import pandas as pd
import sqlite3

# Função para carregar os dados da tabela "expectativa_mercado"
def carregar_dados_banco():
    # Ajuste o caminho para o banco de dados correto
    con = sqlite3.connect("CAMINHO_CORRETO/etlbcb.db")
    query = "SELECT * FROM expectativa_mercado"
    df = pd.read_sql(query, con)
    con.close()
    return df

# Carregar os dados
df = carregar_dados_banco()

# Exportando os dados para um arquivo CSV
csv_file_path = 'expectativa_mercado.csv'  # Caminho do arquivo CSV
df.to_csv(csv_file_path, index=False)

# Exportando os dados para um arquivo Excel
excel_file_path = 'expectativa_mercado.xlsx'  # Caminho do arquivo Excel
df.to_excel(excel_file_path, index=False)

print("Arquivos exportados com sucesso!")
