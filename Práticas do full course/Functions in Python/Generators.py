""" generator functions are a special kind of function that return a lazy iterator. These are objects that you can
loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory. """

""" Normal functions vs generators 
Make use of 'yield' keyword     Make use of 'return' :keyword
Run when 'next()' method is called      Run when name of the method is called
Produce items one at a time and only when required      Produce all the items at once"""

""" Uma generator é como uma função em que você pode pausar para te retornar algo naquele momento e poder continuá-la 
de onde vc parou se vc executá-la de novo (como se tivesse dado um continue nela) O yield é como se fosse um botão de 
pause da função. Ou seja, ele pausa a execução da função e retorna o valor daquele momento mas deixa tudo salvo, 
quando executar a função de novo ela começa a partir daquele yield (como se tivesse dado o play) e só pausa novamente 
quando encontrar outro yield e assim sucessivamente """

def csv_reader(file_name):  # Exemplo de função normal para contar as linhas de um arquivo CSV. Nesse caso ela irá abrir
    # all the arquivo e contar o número de linhas o que pode sobrecarregar a memória
    file = open(file_name)
    result = file.read().split("\n")
    return result


def csv_reader(file_name):  # Exemplo de generator. Aqui abre-se uma linha por vez e por isso não há problemas de
    # sobrecarga
    for row in open(file_name, "r"):
        yield row


def infinite_sequence():
    num = 0
    while num <= 10:
        yield num
        num += 1


for i in infinite_sequence():
    print(i, end=" ")  # Esse end é dizendo que quero que ao finalizar apenas solte um espaço e não quebre a linha
    # como é por padrão

""" Uso da função next() """
next(infinite_sequence())
print("\n")
print("=" * 30)

""" Outro exemplo de generator """


def generator():
    n = 1
    print("Essa é uma função Generator")
    yield n

    n += 1
    print(n, "Segunda volta")
    yield n

    n += 1
    print(n, "terceira volta")
    yield n


a = generator()
print(a)  # <generator object generator at 0x0000007831EF63C0>

next(a)  # Return the next item from the iterator. If default is given and the iterator is exhausted,
# it is returned instead of raising StopIteration.
# Assim que a função executa o yield, ela é pausada e o controle da execução é transferido para quem a chamou.

next(a)  # Dessa vez vai executar a segunda volta, se fosse uma função normal começaria do zero a execução
# Variáveis locais e os seus estados são "lembradas" durante as sucessivas chamadas à função.

next(a)  # Terceira volta

# next(a)     # Quando a função termina, a exceção StopIteration é levantada automaticamente.
# Retorna StopIteration

"""Uma exceção StopIteration é lançada, alertando que a iteração acabou. Ou seja, as variáveis locais NÃO são 
destruídas quando usamos o yield. O objeto Generator só pode ser iterado uma única vez. Se quisermos restartar o 
processo nós precisaremos criar um outro objeto Generator, por exemplo b = generator(). """

print("=" * 30)

# Resetando a função generator.
b = generator()
next(b)
next(b)
next(b)  # Mais que três vezes dá erro StopIteration

print("=" * 30)

"""Também podemos utilizar Generators dentro de um laço for diretamente. Isso porque o laço for também utiliza a 
função next() para iterar e automaticamente encerra a iteração quando a exceção StopIteration é lançada. """

for items in generator():
    print(items)

""" Mais exemplos de generators """
print("=" * 30)


def new(dicio):
    for x, y in dicio.items():
        yield x, y


a = {1: "Hi", 2: "Welcome"}
b = new(a)
print(b)
print(next(b))
print(next(b))
# (next(b)) Executar mais um causa erro de StopIteration por não ter mais dados no dict

print("=" * 30)

""" Generators with loops """
"""To execute the generator function at once (ao invés de ficar escrevendo trocentos next()), you can use 'for' loop. 
This loop iterates over all the objects and after all implementations. It executes the StopIteration """


def ex():
    n = 3
    yield n
    n = n * n
    yield n


v = ex()
for x in v:
    print(x)  # Executa todos os yields, mas mantendo a propriedade das generators

print("=" * 30)

""" Generator Expressions """
""" Create anonymous generators functions like lambda functions """

f = range(6)
# List comprehention
print("List comprehention", end=":")
lista = [x + 2 for x in f]  # List comprehenton usa colchetes
print(lista)  # Retorna a lista bonitinha

print("=" * 12)

print("Generator expression:", end=":")
gener = (x + 2 for x in f)  # Generator expression usa parênteses
print(gener)  # Só vai retornar o objeto

# Pra exibir os valores: usa-se uma estrutura de repetição
for x in gener:
    print(x, end=" ")

print("\n")
print("=" * 30)

""" Usos úteis das generators """

print("Encontrando a sequencia Fibbonatti")


def fib():
    p, s = 0, 1  # Python permite declarar duas variáveis ao mesmo tempo
    while True:
        yield p  # No primeiro loop retorna p = 0, dps p = 1, dps p = 1, dps p = 2, dps p = 5
        p, s = s, p + s


""" O yield é como se fosse um botão de pause da função. Ou seja, ele pausa a execução da função e retorna o valor 
daquele momento mas deixa tudo salvo, quando executar a função de novo ela começa a partir daquele yield (como se 
tivesse dado o play) e só pausa novamente quando encontrar outro yield e assim sucessivamente """

for x in fib():  # Lembrando que o x não é um contador, ele é uma variável que pega os valores gerados pela função,
    # seja ela um range(...) ou qualquer outra como esta. x é o valor retornado, ou seja o p em dados instantes.
    if x > 50:
        break
    print(x, end=" ")

print("\n")
print("=" * 30)


# function version
def fibon(n):
    a1, b2 = 0, 1
    result = []
    for indice in range(n):
        result.append(a1)
        a1, b2 = b2, a1 + b2
    return result


print("Squencia Fibbonatti: ", fibon(12))

print("=" * 30)
""" Imprimindo números em sequencia"""

b = (x for x in range(1, 100, 2))
print(b)  # Lembrando que é uma expression generator, vai retornar o objeto. Os dados são mostrados em uma repetição
for y in b:
    print(y, end=" ")

print("\n")
print("=" * 30)
