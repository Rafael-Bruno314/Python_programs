"""List Comprehensions """
""" List Comprehension foi concebida na PEP 202 e é uma forma concisa de criar e manipular listas.
Sua sintaxe básica é: [expr for item in lista] """

# Forma normal de fazer uma lista
lista = list()
for item in range(10):
    lista.append(item ** 2)  # Retorna o quadrado dos números de 0 a 9
print(lista)

# Forma usando list comprehension
lista = [item ** 2 for item in range(10)]   # Eu vou preenchendo a lista a partir do momento em que ela é criada
print(lista)

"""List Comprehensions com if  [expr for item in lista if cond]"""
resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
print(resultado)

# Imprimindo os ímpares de 1 a 99 com list comprehention
print([x for x in range(1, 100, 1) if x % 2 != 0])

# Jeito de imprimir todos os ímpares de 1 a 99 em uma linha usando filter() e lambda
print(list(filter(lambda x: x % 2 != 0, range(1, 100, 1))))

# Forma mais fácil de todas disparado
print(list(range(1, 100, 2)))
