#Objetivo:
#Calcular a razão de duas áreas de dois quadrados pelo método de monte carlo

import numpy as np
import time


def cria_sq(sq_size):
    square = np.empty((0, 2),int)  # Inicializa um array vazio para armazenar as coordenadas (x, y)

    for coord_x in range(1, sq_size+1):
        for coord_y in range(1, sq_size+1):
            coordenadas = np.array([[coord_x, coord_y]])
            square = np.append(square, coordenadas, axis=0)
    return square


def razao_Area(interacao,limite_maior,limite_menor):
    print(interacao,limite_maior,limite_menor)
    x = np.random.randint(1,limite_maior+1,interacao)
    y = np.random.randint(1,limite_maior+1,interacao)
    dentro_quadrado = np.sum((x <= limite_menor) & (y <= limite_menor))
    return dentro_quadrado/interacao


t1 = time.time()
sq_maior = cria_sq(1000)
sq_menor = cria_sq(500)
interacao = 1000

print(f"A razão entre os dois quadrados pelo método de Monte Carlo com {interacao} interações foi de {razao_Area(interacao,sq_maior[-1][0],sq_menor[-1][0])}")
t2 = time.time()

print(f"O tempo gasto pra executar o programa foi de {t2 - t1}segundos")
