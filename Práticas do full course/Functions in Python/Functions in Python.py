def func1(name):
    return f"Hello {name}"


def func2(name):
    return f"{name}, how you  doing?"


def func3(func4):
    return func4('Dear banana')     # Executo o que vai ser chamado de func4 aqui dentro com o parâmetro 'Dear banana'


""" O que na func3 é func4, o parâmetro, eu insiro a func1, sendo assim a func4 é na verdade a func1. Portanto, a func3
recebe como parâmetro a func1 e assim retorna a func1 com o parâmetro 'name' como o Dear banana.
# É um pouco confuso de primeira mas se pega o jeito """
print(func3(func1))

""" Aqui a mesma coisa, a func3 retorna a func4 que é seu parâmetro, mas ele é na verdade a func2 e recebendo o
parâmetro name como Dear banana. """
print(func3(func2))

print("=" * 30)
""" Nested functions - function inside function"""


def func():
    print("first function")

    def func_child1():
        print("first child function")

    def func_child2():
        print("second child function")

    func_child2()  # Just it to run a function in the program
    func_child1()


func()  # Only it. Simple, right?

print("=" * 30)


def func(n):
    def func11():
        return "banana"

    def func12():
        return "gold"

    if n == 1:
        return func11()
    else:
        return func12()


a = func(2)
b = func(1)
print(a)
print(b)

print("=" * 30)

""" 'Criador' de funções de potência """


def cria_potencia(x):  # 3 - Com x = 3 e ela retorna a própria função potencia que vai precisar de 'num'
    def potencia(num):  # Esse 'num' seria o 2. Pois x já é 3
        return x ** num

    return potencia


# Potência de 2 e 3
potencia_2 = cria_potencia(2)
potencia_3 = cria_potencia(3)  # 2- Inicia a função cria_potencia com parâmetro 3 e um 2 que está na variável

# Resultado
print(potencia_2(2))
print(potencia_3(2))  # 1- imprimir variável com parâmetro 2
