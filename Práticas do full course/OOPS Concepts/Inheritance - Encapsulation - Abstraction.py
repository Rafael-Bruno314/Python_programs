""" Herança (inheritance) """
"""A class can inherit attributes and behavior methods from another class (parent class)"""
"""Uma classe que herda de uma super-classe é chamada sub-class , heir class ou child class"""
""" Existem 4 tipos de herança:
        simples: uma classe pai e uma classe filha
        múltipla: mais de uma classe pai - como a que fiz, uma classe filha que tem dois pais (SuperCar e SuperCarMae) 
        multinível: avô -> pai -> neta, uma classe que é filha de uma e pai de outra
        Hierárquico: quando há mais de um tipo de herança presente"""


class SuperCar:     # Classe pai
    def __init__(self, modelname, year_prod, price):  # Essa é a função 'constructor'!!!
        self.modelname = modelname  # O self serve para referenciar o próprio objeto que formos criar, seja ele qual for
        self.year_prod = year_prod
        self.price = price
        # All the objeto criado terá esses três atributos

    def price_inc(self):
        self.price = int(self.price * 1.5)  # I int é só pra tirar o .0 quee fica no final do valor


class SuperCarMae:
    pass


class SubCar(SuperCar, SuperCarMae):     # Declarando uma classe filha, dentro do parênteses dizendo quem são os pais
    def __init__(self, modelname, year_prod, price, cc):
        SuperCar.__init__(self, modelname, year_prod, price)    # Estou pegando os atributos construídos da classe pai,
        # que já estão prontos e não precisar repetir código

        # super().__init__(modelname, year_prod, price)   # também funciona para essa finalidade. Esse super() é uma
        # super função que pega os métodos da classe pai
        self.cc = cc    # Estou adicionando novos atributos exclusivos da classe filha


honda = SubCar("city", 2017, 10000, 150)

print(honda.modelname)      # Ela olha na classe filha, da qual o objeto foi criado, se não encontrar ela procura na
# classe pai. Ou seja, a herança é uma classe, por padrão, já ter os constituintes da classe pai. Por exemplo,
# uma classe humano teria algumas características herdadas da super classe mamífero.
# Nota: quando fiz essa linha a classe filha não tinha nenhum construtor, apenas o 'pass'

print(honda.cc)

print("="*30)

print(help(honda))      # A função help() mostra informações detalhadas sobre algo

print("="*30)

""" Abstraction """
""" Hides the implementation details and only provides the functionality to the user"""
""" Uso de classes abstratas (abstract class) e Interfaces"""

"""Classe abstrata: classe que não produz objetos. Ela é apenas a classe pai de filhas que herdam suas 
características e essas sim produzem os objetos """

print("="*30)

""" Super functions - super() """


class Parent:
    def func1(self):
        print("This is function 1")


class Child(Parent):
    def func2(self):
        super(Child, self).func1()      # Esse Child, self dentro da super() vem por padrão
        # super().func1()               # São idênticos
        print("This is function 2")


ob = Child()
ob.func2()

print("="*30)

""" Method Overriding """
"""Muuito simples, basta chamar o método da classe filha com o mesmo da classe pai, assim o programa vai dar 
prioridade para executar o método da filha e não a do pai, e assim, parabéns, sobreescreve um método da classe pai. """


class Parent1:
    def func1(self):
        print("This is function 1")


class Child1(Parent1):
    def func1(self):
        print("This is function 2")


ob1 = Child1()
ob1.func1()     # Vai imprimir a '... function 2' even the father class having the same metod
