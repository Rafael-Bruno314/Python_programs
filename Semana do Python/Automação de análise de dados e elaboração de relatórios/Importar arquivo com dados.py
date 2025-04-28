import pandas as pd
import os

df = pd.read_excel(os.path.join(os.path.dirname(__file__), 'Vendas - Dez.xlsx'))

print(df)

faturamento = df['Valor Final'].sum()
qt_produtos = df['Quantidade'].sum()

print("O faturamento foi de: R$ {0:,.2f}".format(faturamento))
print(f"A quantidade de produtos vendida foi de: {qt_produtos:,}")
