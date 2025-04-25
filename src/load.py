import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Função criada para salvar um DataFrame como um arquivo CSV.

    Parâmetros:
        df (pd.DataFrame): O DataFrame que deve ser salvo.
        nome_arquivo (str): Caminho e nome do arquivo de saída (ex: 'dados.csv').
        separador (str): Caractere usado como separador de colunas no CSV (ex: ',' ou ';').
        decimal (str): Caractere usado para representar o ponto decimal (ex: '.' ou ',').

    Saída esperada:
        O DataFrame deve ser salvo em um arquivo .csv dentro da pasta de datasets.

    """
    
    df.to_csv(nome_arquivo, sep=separador, decimal= decimal)
    return


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """
    Salva um DataFrame em uma tabela de um banco de dados SQLite.

    Parâmetros:
        df (pd.DataFrame): O DataFrame a ser salvo no banco de dados.
        nome_banco (str): O nome (ou caminho) do arquivo do banco de dados SQLite.
        nome_tabela (str): O nome da tabela onde os dados serão armazenados.

    Saída esperada:
        O DataFrame deve ser salvo em um arquivo .sqlite ou .db ou atualizado, se já existir. 

    """

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()

    return


def salvarMySql(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    """
    Salva um DataFrame em uma tabela de um banco de dados MySQL.

    Parameters:
        df (pd.DataFrame): O DataFrame a ser salvo no banco de dados.
        usuario (str): Nome de usuário do banco de dados MySQL.
        senha (str): Senha do usuário do banco de dados.
        host (str): Endereço do servidor onde o banco está hospedado.
        banco (str): Nome do banco de dados MySQL.
        nome_tabela (str): Nome da tabela onde os dados serão armazenados.

    Saída esperada:
        A função irá estabelecer conexão com o banco de dados MySQL e o DataFrame deve ser salvo como uma tabela no banco de dados especificado.
    """

    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
