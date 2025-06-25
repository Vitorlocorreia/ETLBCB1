import requests
import pandas as pd
import sqlite3

def requestApiBcb(data: str) -> pd.DataFrame:
    """
    Função para extrair os dados da API do Banco Central (Meios de Pagamento).

    Parâmetros:
    data - string - AAAAT (Exemplo: 20191)

    Saída:
    DataFrame - Estrutura de dados do pandas
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    dados = req.json()

    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])
    return df


def requestExpectativaApi() -> pd.DataFrame:
    """
    Função para extrair os dados da nova API do Banco Central (Expectativas de Mercado).

    Saída:
    DataFrame - Estrutura de dados do pandas
    """
    url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=100&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    dados = req.json()

    # Transformar os dados da nova API
    df = pd.json_normalize(dados["value"])
    
    # Agora usamos o nome correto da coluna "Data"
    df["Data"] = pd.to_datetime(df["Data"])  # Ajuste de data usando a coluna correta
    return df


def salvar_dados_no_banco(df_novo: pd.DataFrame):
    """
    Função para salvar os dados da API na tabela do banco de dados.
    
    Parâmetros:
    df_novo - DataFrame - Dados a serem salvos no banco
    """
    # Conectar ao banco de dados
    con = sqlite3.connect("src/datasets/etlbcb.db")
    
    # Criar ou substituir a tabela "expectativa_mercado" com os dados da API
    df_novo.to_sql("expectativa_mercado", con, if_exists="replace", index=False)
    
    # Fechar a conexão com o banco
    con.close()
    
    print("Tabela 'expectativa_mercado' criada e dados inseridos com sucesso!")


# Obtendo os dados da nova API
df_novo = requestExpectativaApi()

# Verifique se os dados foram extraídos corretamente
if df_novo is not None:
    # Salvar os dados no banco de dados
    salvar_dados_no_banco(df_novo)
else:
    print("Falha ao obter dados da API.")
