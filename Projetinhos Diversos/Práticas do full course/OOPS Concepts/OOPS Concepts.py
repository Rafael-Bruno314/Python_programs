"""A class is the blueprint from which specific objects are created"""

""" Instancias da classe = objetos"""


class Car:  # Classe Car, prazer
    pass


honda = Car()  # Objetos da classe, prazer
tata = Car  # Parece que nesse caso os parênteses são redundantes

honda.modelname = "City"
honda.year_prod = 2018  # Jeito idiota de criar características (métodos e propriedades) para os objetos
honda.price = 10000  # .price = método / 10000 = propriedade

tata.year_prod = 2017

print(honda.price)  # Output: 10000
print("=" * 30)

""" Criando contrutores das classes """
""" São funções responsáveis por 'construir' os métodos dos objetos,
os construtores são o jeito inteligente de criar os objetos"""

""" Atributos = características do objeto: se ele é azul, quanto custa, qual o nome etc """
""" Métodos = ações do objeto: se ele anda, corre, envia algo, buzina etc"""


class Car:
    def __init__(self, modelname, year_prod, price):  # Essa é a função 'constructor'!!!
        self.modelname = modelname  # O self serve para referenciar o próprio objeto que formos criar, seja ele qual for
        self.year_prod = year_prod
        self.price = price
        # All the objeto criado terá esses três atributos

    def price_inc(self):
        self.price = int(self.price * 1.5)  # I int é só pra tirar o .0 que fica no final do valor


honda = Car('City', 2017, 100000)
tata = Car('Bolt', 2016, 30000)

honda.cc = 1500  # You can create new attributes out of class without problems

print("Preço do Honda: ", honda.price, "\n")
print(honda)  # Retorna que é um objeto da classe Car
print(honda.__dict__)  # Para ver todos os atributos associados a um objeo

honda.price_inc()
print("Novo preço do Honda: ", honda.price)
