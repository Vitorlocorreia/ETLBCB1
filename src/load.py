import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, dec: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=dec)
    return


def salvarSqlite(df: pd.DataFrame, nome_banco: str, nome_tabela):
    conn = sqlite3.connect(nome_banco)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()
    return


def salvarMySql(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
    return
