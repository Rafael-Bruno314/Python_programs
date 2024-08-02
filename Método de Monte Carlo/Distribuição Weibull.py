import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Dados amostrais
dados_amostrais = np.array([45, 50, 55])

# Ajustar a distribuição de Weibull aos dados amostrais
params = weibull_min.fit(dados_amostrais, floc=0)
k, loc, lambda_ = params

# Gerar simulações de Monte Carlo
num_simulacoes = 10000
simulacoes = weibull_min.rvs(k, loc, lambda_, size=num_simulacoes)

# Calcular a média das simulações
media_simulacoes = np.mean(simulacoes)

# Plotar a distribuição das simulações
plt.hist(simulacoes, bins=50, density=True, alpha=0.6, color='g')
plt.axvline(media_simulacoes, color='r', linestyle='dashed', linewidth=2)
plt.title('Distribuição das Simulações de Monte Carlo (Weibull)')
plt.xlabel('Resistência à Flexão (MPa)')
plt.ylabel('Frequência')
plt.show()

print(f"Média das Simulações: {media_simulacoes:.2f} MPa")
print(f"Parâmetros de Weibull: k = {k:.2f}, lambda = {lambda_:.2f}")
