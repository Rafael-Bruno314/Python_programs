""" Lambda functions are anonymous or nameless functions.
Lambda is not a name, but a keyword
Also knows as throw-away functions. Functions which are used one time.
Main use: passed as inputs or returned as outputs of high-order functions
The body of Lambda functions is written in a single line """

x = lambda a1: a1 * a1  # Jeito original de fazer lambda, mas que o corno do PEP8 avisa que tá errado


def f(a1): return 2 * a1  # Jeito alternativo de imprimir o sem aviso


print(f(3))
print(x(3))
print("=" * 30)

""" Lambda within user-defined functions """


def a(x2):
    return lambda y: x2 + y


t = a(4)
print(t(8))
print("=" * 30)

""" Using Lambda functions within filter(), map() and reduce() 
Very important building functions """

print("filter() - used to filter the given interables (lists, sets etc) with the help of another function (lambda) "
      "passed as an argument to test all elements to be true or false and re-printed. That is, creates an output list "
      "consisting of values for which the function returns true")

mylist = [1, 2, 3, 4, 5, 6]
newlist = list(filter(lambda a3: (a3 / 3 == 2), mylist))  # filter(function, interable)
print(newlist)

print("\nmap() - applies a given function (lambda) to all the interables and returns a new list with the statements "
      "are true or false.")

mylist = [1, 2, 3, 4, 5, 6]
p = list(map(lambda a4: (a4 / 3 == 2), mylist))
print(p)

print("=" * 12)

""" map() faz uma ação usando o interador como parâmetro e gera outra lista de resultado."""


# map(func, lista/interavel)


def new(a6, b):
    return a6 * b


x4 = map(new, [1, 2, 3, 4], [1, 2, 4, 5])
"""Nesse caso, a map() executa uma função (new) tendo como parâmetros as duas listas (a6, b), faz a ação para cada 
termo delas e gera uma lista com o resultado. Nesse caso, ela somou os valores de cada elemento de uma lista com o da 
outra e gerou uma lista com a soma deles """
print(x4)
print(list(x4))

print("\nreduce - define uma função onde o interável (lista, no caso) é passado como parâmetros para essa função como "
      "um parâmetro e retorna um único valor. Ou seja, reduz a lista para um único valor dentro de um sentido/ordem "
      "especificado.")

from functools import reduce

r = reduce(lambda a5, b: a5 + b, [1, 2, 3, 4, 5, 6])
# Basically, it's a recursive function that sums all the list
print(r)

print("=" * 30)

print("Using lambda to solve some algebric equations")


# 3x + 4y
# d = lambda x1, y1: 3 * x1 + 4 * y1
def d(x1, y1): return 3 * x1 + 4 * y1


print(d(4, 2))  # Returns 20

print("=" * 30)

""" map and filter within reduce """
r = reduce(lambda x3, y3: x3 + y3, map(lambda x3: x3 + x3, filter(lambda x3: x3 <= 4, list((1, 2, 3, 4, 5, 6, 7, 8)))))
print(r)  # Combinação de funções construtoras. Output = 20
""" 
filter() - vai filtrar os elementos maiores que 4 da lista - (1, 2, 3, 4)
map() - vai pegar essa lista como parâmetro x3 e vai somar todos os termos com eles mesmos - (1+1, 2+2, 3+3, 4+4)
reduce() - vai pegar os valores da lista e somá-los formando um único número - (2 + 4 + 6 + 8) = 20
"""
