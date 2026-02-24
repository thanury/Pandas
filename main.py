import pandas as pd
import numpy as np

df_vendas = pd.read_csv("vendas_tech.csv", encoding="utf-8")
print(df_vendas)

df_gerentes = pd.read_excel("gerentes_lojas.xlsx")
print(df_gerentes)