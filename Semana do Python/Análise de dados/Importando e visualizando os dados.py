import pandas as pd

df = pd.read_csv(r'telecom_users.csv')

# Excluindo uma coluna da visualização
df = df.drop(["Unnamed: 0"], axis=1)

print(df)

