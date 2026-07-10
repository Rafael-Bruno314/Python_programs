import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Dados amostrais de resistência à flexão (em MPa)
dados_amostrais = np.array([45, 50, 55])  # Valores de exemplo - substitua por seus dados reais

#-------------------------------------------------------------------------------
# Ajuste da distribuição de Weibull aos dados amostrais
# Parâmetros:
#   floc=0: Fixa o parâmetro de localização (loc) em 0 para simplificar o modelo
# Retorna:
#   Tupla (k, loc, lambda_), onde:
#     k (shape): Parâmetro de forma da Weibull (indica a "dispersão" dos dados)
#     loc: Parâmetro de localização (fixado em 0)
#     lambda_ (scale): Parâmetro de escala (relacionado à vida característica)
#-------------------------------------------------------------------------------
params = weibull_min.fit(dados_amostrais, floc=0)
k, loc, lambda_ = params  # Desempacota os parâmetros ajustados

#-------------------------------------------------------------------------------
# Simulação de Monte Carlo baseada na distribuição de Weibull ajustada
#-------------------------------------------------------------------------------
num_simulacoes = 10000  # Número de simulações (aumente para maior precisão)
simulacoes = weibull_min.rvs(k, loc, lambda_, size=num_simulacoes)  # Gera valores aleatórios

# Calcula a média das simulações (estimativa pontual da resistência média)
media_simulacoes = np.mean(simulacoes)

#-------------------------------------------------------------------------------
# Visualização dos resultados
#-------------------------------------------------------------------------------
plt.hist(simulacoes, bins=50, density=True, alpha=0.6, color='g', label='Simulações')
plt.axvline(media_simulacoes, color='r', linestyle='dashed', linewidth=2, label=f'Média: {media_simulacoes:.2f} MPa')
plt.title('Distribuição das Simulações de Monte Carlo (Weibull)')
plt.xlabel('Resistência à Flexão (MPa)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.show()

#-------------------------------------------------------------------------------
# Saída dos resultados numéricos
#-------------------------------------------------------------------------------
print(f"Média das Simulações: {media_simulacoes:.2f} MPa")
print(f"Parâmetros de Weibull: k = {k:.2f}, lambda = {lambda_:.2f}")
