import pandas as pd
import sqlite3

# Função para carregar os dados da tabela "expectativa_mercado" no banco SQLite
def carregar_dados_banco():
    con = sqlite3.connect("src/datasets/etlbcb.db")  # Substitua pelo caminho correto do seu banco de dados
    query = "SELECT * FROM expectativa_mercado"
    df = pd.read_sql(query, con)
    con.close()
    return df

# Carregar os dados da tabela "expectativa_mercado"
df = carregar_dados_banco()

# Salvar os dados em um arquivo CSV
df.to_csv('expectativa_mercado.csv', index=False)

print("Arquivo CSV gerado com sucesso!")
