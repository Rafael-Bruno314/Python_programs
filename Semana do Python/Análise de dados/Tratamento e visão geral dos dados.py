import pandas as pd

df = pd.read_csv(r'C:\Users\1234\Downloads\telecom_users.csv')

# Excluindo uma coluna da visualização
df = df.drop(["Unnamed: 0"], axis=1)

print(df.info())

# Transformar coluna que está como objeto e deveria ser número
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors='coerce')
# If 'coerce', then invalid parsing will be set as NaN.

# Removendo coluna(s) que está 100% vazia
df = df.dropna(how='all', axis=1)

# Remover linhas que tenham algum item vazio
df = df.dropna()

print(df.info())
print(df)

# Determinando encerramento de contratos
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True))
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
