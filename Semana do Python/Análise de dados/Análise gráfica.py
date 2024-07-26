import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\1234\Downloads\telecom_users.csv')
df = df.drop(["Unnamed: 0"], axis=1)
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors='coerce')
df = df.dropna(how='all', axis=1)
df = df.dropna()
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

"""for coluna in df:
    if coluna != "IDCliente":
        # Criar o gráfico
        fig = px.histogram(df, x=coluna, color="Churn")
        # Exibir o gráfico
        fig.show()
        print(df.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])
"""

fig = px.histogram(df, x="ServicoSegurancaOnline", color="Churn")
fig.show()
print(df.pivot_table(index="Churn", columns="ServicoSegurancaOnline", aggfunc='count')["IDCliente"])
