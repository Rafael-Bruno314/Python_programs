import random
import numpy as np

#O resultado não faz sentido nenhum

# Parâmetros dos materiais
resistencia_tração_al = 250  # Resistência à tração do alumínio (MPa)
resistencia_tração_cu = 210  # Resistência à tração do cobre (MPa)
resistencia_tração_mg = 350  # Resistência à tração do magnésio (MPa)

# Função para calcular a resistência à tração da liga com a Lei de Misturas
def resistencia_tracao(composicao):
    """
    Calcula a resistência à tração da liga usando a Lei de Misturas.
    """
    alumino, cobre, magnesio = composicao
    # Resistência à tração dos componentes
    sigma_al = resistencia_tração_al
    sigma_cu = resistencia_tração_cu
    sigma_mg = resistencia_tração_mg
    
    # Lei de Misturas
    resistencia = alumino * sigma_al + cobre * sigma_cu + magnesio * sigma_mg
    return resistencia

# Função para gerar uma população inicial
def gerar_populacao(tamanho_populacao, num_elementos):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = [random.uniform(0, 1) for _ in range(num_elementos)]
        soma = sum(individuo)
        individuo = [x / soma for x in individuo]  # Normaliza para que a soma das porcentagens seja 1
        populacao.append(individuo)
    return populacao

# Função de seleção por torneio
def selecao(populacao):
    torneio_size = 5
    torneio = random.sample(populacao, torneio_size)
    torneio.sort(key=lambda x: resistencia_tracao(x), reverse=True)
    return torneio[0]

# Função de cruzamento (crossover)
def cruzamento(pai, mae):
    ponto_corte = random.randint(1, len(pai) - 1)
    filho1 = pai[:ponto_corte] + mae[ponto_corte:]
    filho2 = mae[:ponto_corte] + pai[ponto_corte:]
    return filho1, filho2

# Função de mutação
def mutacao(individuo, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        idx = random.randint(0, len(individuo) - 1)
        individuo[idx] = random.uniform(0, 1)
        soma = sum(individuo)
        individuo = [x / soma for x in individuo]  # Normaliza
    return individuo

# Algoritmo Genético
def algoritmo_genetico(tamanho_populacao, num_geracoes, taxa_mutacao=0.1):
    populacao = gerar_populacao(tamanho_populacao, 3)  # 3 materiais: Alumínio, Cobre, Magnésio
    melhores_individuos = []
    
    for geracao in range(num_geracoes):
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pai = selecao(populacao)
            mae = selecao(populacao)
            filho1, filho2 = cruzamento(pai, mae)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(mutacao(filho2, taxa_mutacao))
        
        # Avaliar a população e manter os melhores indivíduos
        populacao = sorted(nova_populacao, key=lambda x: resistencia_tracao(x), reverse=True)[:tamanho_populacao]
        melhores_individuos.append(populacao[0])
    
    melhor_composicao = melhores_individuos[-1]
    return melhor_composicao, resistencia_tracao(melhor_composicao)

# Parâmetros do Algoritmo Genético
tamanho_populacao = 500
num_geracoes = 1000

# Executando o Algoritmo Genético
melhor_composicao, melhor_resistencia = algoritmo_genetico(tamanho_populacao, num_geracoes)

print(f"Melhor composição encontrada: Alumínio = {melhor_composicao[0]:.3f}, Cobre = {melhor_composicao[1]:.3f}, Magnésio = {melhor_composicao[2]:.3f}")
print(f"Melhor resistência à tração: {melhor_resistencia:.3f} MPa")
