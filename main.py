import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSqlite, salvarMySql

dadosBcb = requestApiBcb("20191")

# salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";",".")

salvarSqlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

# salvarMySql(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamentos_tri")

