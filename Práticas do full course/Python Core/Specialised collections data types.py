# This are not all the specialised collections, only the best
from collections import ChainMap
from collections import Counter
from collections import defaultdict

print("namedtuple factory function for creating tuple subclasses with named fields")
print("deque list-like container with fast appends and pops on either end")
print("ChainMap dict-like class for creating a single view of multiple mappings")
print("Counter dict subclass for counting hashable objects")
print("OrderedDict dict subclass that remembers the order entries were added")
print("defaultdict dict subclass that calls a factory function to supply missing values")
print("UserDict wrapper(embrulha/empacota/junta) around dictionary objects for easier dict subclassing")
print("UserList wrapper around list objects for easier list subclassing")
print("UserString wrapper around string objects for easier string subclassing")

print("=" * 30)

a = {1: 'Rafael', 2: 'Bruno'}
b = {3: 'Engenharia', 4: 'de Materiais'}

together = ChainMap(a, b)   # Ela meio que coloca dicionários juntos dentro de uma tuple
print(type(together))
print(together)

print("=" * 30)

a = [1, 1, 3, 4, 5, 1, 2, 4, 5, 6, 2, 2, 1, 2, 3, 4, 1, 2, 3, 4]
c = Counter(a)  # Basicamente transforma essa lista em um dicionário onde a key é o termo da lista e o value é a
# quantidade de vezes que esse termo se repete na lista
print(c)

print(sorted(c.elements()))
""" Esse interador (sentido de percorredor) pega todos os termos dentro do counter e o trata como se fosse uma lista de
termos """
print("um iterador se refere ao comando/objeto/algo que permite ao programador percorrer um container (coleção de "
      "dados/valores")

a.sort()    # Works in the same way
print(a)

print("=" * 30)

print("Criando um número a partir de seus fatores primos (Knuth's example):")
prime_factors = Counter({2: 2, 3: 3, 17: 1})
print(prime_factors)
product = 1

for factor in prime_factors.elements():     # loop over factors
    # print(factor)
    product *= factor                       # and multiply them
print(product)

print("=" * 30)

d = defaultdict(int)
d['arroz'] = 'python'
d[95] = 'banana'
print(type(d))

print(d['arroz'])     # Keys estranhas só pra lembrar que dict Não é ordenado!
print(d[95])
print(d[3])
"""Return '0' but should be an error if it were a normal dictionary pois a defaultdict é uma subclasse de dict (do 
dicionário) que chama uma função fábrica (ou construtora) para fornecer valores ausentes. Na verdade retornou 0 pois 
disse que os dados do dict eram int, se eu disse que eram strings retornava vazio, mas da mesma forma não dá erro 
como daria em um dict normal """
