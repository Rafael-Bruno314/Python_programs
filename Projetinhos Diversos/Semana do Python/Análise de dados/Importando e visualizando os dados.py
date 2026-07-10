import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'telecom_users.csv'))

# Excluindo uma coluna da visualização
df = df.drop(["Unnamed: 0"], axis=1)

print(df)