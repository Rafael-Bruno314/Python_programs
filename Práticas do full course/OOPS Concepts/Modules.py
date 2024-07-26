# Modules in python is just split the code and import in the main program using the 'import' keyword

"""Importando módulos próprios, criados pelo usuário"""

"""
Importando o módulo calculadora. Há três formas de importar
import calculadora-módulo - importa tudo e tem-se que declarar as funções como pertencendo ao módulo
import calculadora-módulo as calc - a mesma coisa, mas alterando o nome (method with alias)
from  calculadora-módulo import * - importa todas as classes e funções e por isso não precisa de avisar que pertence a
                                    determinado módulo
from calculadora-módulo import add - importa apenas a função 'add' - como pegar um livro apenas de uma biblioteca
"""

import calculadora_módulo as calc

print(help(calc))

print("=" * 12)

print(calc.add(10, 5))
print(calc.subt(10, 5))
print(calc.product(10, 5))
print(calc.division(10, 5))

print("=" * 30)

"""
Importando módulos já embutidos no python, built-in modules in python

Built-in modules are written in C and interpreted using the python interpreter
"""

print(help('modules'))  # Essa função mostra todos os built-in modules in python

print("=" * 30)

# Direct function - dir() - Exibe os nomes dos métodos, variáveis e funções dentro de um determinado módulo
print(dir(calc))

print("=" * 30)

"""
Python Modules - Search path

When we import a module, Python searches for the module at certains places. If it cannot find the module in the 
built-in modeles, it searches through the list in the sys.paty 

Path of search:
    Current directory --> PYTHONPATH --> Defaut Directory

Ou seja, o python já pega automaticamente onde o módulo está 
"""

print("Alguns módulos padrões interessantes: ")

import sys

print(sys.path)  # Exibe o caminho de todos os módulos que o programa tem

print("=" * 30)

import math

print(math.factorial(5))
print(math.sinh(1))

import random

print(random.randrange(0, 5))

import datetime

print(datetime.datetime.now())
