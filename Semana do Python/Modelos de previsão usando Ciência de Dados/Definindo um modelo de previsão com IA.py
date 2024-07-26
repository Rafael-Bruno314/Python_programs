from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("advertising.csv")

x = df.drop('Vendas', axis=1)
y = df['Vendas']

# Começando o treinamento da IA
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Treinando a IA com dois métodos estatísticos diferentes
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor()
rf_reg.fit(x_train, y_train)

# Testando a IA (com 30% dos dados restantes)
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_test, test_pred_lin))
print(f"R^2 da Regressão linear: {r2_lin}")
print(f"Desvio quadrático médio (RSME) da Regressão linear: {rmse_lin}")

r2_rf = metrics.r2_score(y_test, test_pred_rf)
rmse_rf = np.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))
print(f"R^2 da Random Forest: {r2_rf}")
print(f"Desvio quadrático médio (RSME) da Random Forest: {rmse_rf}")

# Criando uma tabela para mostrar os resultados dos testes
df_resultado = pd.DataFrame()
df_resultado['y_teste'] = y_test
df_resultado['y_previsao_lin'] = test_pred_lin
df_resultado['y_previsao_rf'] = test_pred_rf

print(df_resultado)

fig = plt.figure(figsize=(15, 5))
sns.lineplot(data=df_resultado)
plt.show()

# Definindo de uma vez a importância de cada meio de comunicação
importancia_features = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
plt.figure(figsize=(5, 5))
sns.barplot(x=importancia_features.index, y=importancia_features[0])
plt.show()
