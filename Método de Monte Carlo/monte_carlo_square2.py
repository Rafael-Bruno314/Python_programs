#Objetivo:
#Calcular a razão de duas áreas de dois quadrados pelo método de monte carlo

import random
import numpy
import time

def cria_sq(sq_size):
    x,y,square = [],[],[]
    for coord_x in range(1,sq_size+1):
        for coord_y in range(1,sq_size+1):
            square.append((coord_x,coord_y))
    return square

def razao_Area(interacao,limite_maior,limite_menor):
    j=0
    for i in range(1,interacao):
        x = random.randint(1,limite_maior)
        y = random.randint(1,limite_maior)
        if(x<=limite_menor and y<=limite_menor):
            j+=1
    return j/interacao

t1 = time.time()
sq_maior = cria_sq(10000)
sq_menor = cria_sq(1000)
interacao = 1000

print(f"A razão entre os dois quadrados pelo método de Monte Carlo com {interacao} interações foi de {razao_Area(interacao,sq_maior[-1][0],sq_menor[-1][0])*100}%")
t2 = time.time()

print(f"O tempo gasto pra executar o programa foi de {t2 - t1}segundos")

