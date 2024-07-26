import pandas as pd

tabela = pd.read_excel(r'C:\Users\1234\Downloads\Produtos.xlsx')
print(tabela)

cotacao_dolar = 5.48
cotacao_euro = 6.62
cotacao_ouro = 312.81

# Alterando dados de células
tabela.loc[tabela["Moeda"] == "Dolar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# Atualizando tabelas com novos cálculos
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print("="*30)
print(tabela)

# Exportando o resultado para uma planilha Excel
tabela.to_excel("Produtos Novos.xlsx", index=False)
