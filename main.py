import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySql

dados_bcb = requestApiBcb("20191")
# salvarCsv(dados_bcb, 'ETLbcb/src/datasets/meiosPagamentosTri.csv', ';', '.')

# salvarSQLite(dados_bcb, "ETLbcb/src/datasets/ETLbcb.db", "meios_pagamentos_tri")

salvarMySql(dados_bcb, "root", "teste", "localhost", "etlbcb", "meios_pagamentos_tri")
