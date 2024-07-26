import pandas as pd

df = pd.read_excel(r'Vendas - Dez.xlsx')
print(df)

faturamento = df['Valor Final'].sum()
qt_produtos = df['Quantidade'].sum()

print("O faturamento foi de: R$ {0:,.2f}".format(faturamento))
print(f"A quantidade de produtos vendida foi de: {qt_produtos:,}")
