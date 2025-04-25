import requests
import pandas as pd

def requestApiBcb(data: str) -> pd.DataFrame:
    """
    Função para extrair os dados do meio de pagamentos trimestrais da API do Banco Central

    Parâmetros:
        data - string: aaaat(Exemplo: 20191)

    Saída:
        DataFrame - Estrutura de dados do Pandas
    """

    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"

    req = requests.get(url)
    dados = req.json()

    df = pd.json_normalize(dados["value"])

    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])

    return df
