import time

""" O conceito de decorator provê uma maneira simples de modificar
o comportamento de uma função sem necessariamente alterá-la.
 Decorator nada mais é que um método para envolver uma função, modificando seu comportamento."""

""" Versão sem uso do recurso único do python (@) """


def decorator(function):  # 3 - essa function é a other_function e essa decorator não faz nada só ativa o seu return
    def wrapper():
        print("Estou antes da execução da função passada como argumento")
        function()  # 5 - Executa tudo que está na other_function
        print("Estou depois da execução da função passada como argumento")

    return wrapper  # 4 - Executa a função filha wrapper (embrulho)


def other_function():
    print("Sou um belo argumento!")


funcao_decorada = decorator(other_function)  # 2 - Ativa a função passando como parâmetro a other_function
funcao_decorada()  # 1 - ativa a variável, lembrando que tudo em python é um objeto
# 6 - Imprime o resultado após seguir esse caminho de 1 a 5.
# Dessa forma, conseguimos adicionar qualquer comportamento antes e depois da execução de uma função qualquer!


print("=" * 30)
""" Versão com o @ """


def decorator(function):  # 3 - essa function é a other_function e essa decorator não faz nada só ativa o seu return
    def wrapper():
        print("Estou antes da execução da função passada como argumento")
        function()  # 5 - Executa tudo que está na other_function
        print("Estou depois da execução da função passada como argumento")

    return wrapper  # 4 - Executa a função filha wrapper (embrulho)


@decorator  # Manda essa other_function como um parâmetro para a decorator e a executa
def other_function():
    print("Sou um belo argumento!")


other_function()

print("=" * 30)

""" Calculating the time of execution of any function """


# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))   # Jeito alternativo de exibir algo com print()
        )

    return wrapper


# Decora a função com o decorator

""" Esse arroba é a forma fácil do python que significa que esssa função main é "decorada" pela calcula_duracao, 
ou seja, vai executar:
1 - a função calcula_duracao com a main como parâmetro
2 - calcula_duracao ativa a wrapper e imprime o resultado """

""" @calcula_duracao == funcao_decorada = decorator(other_function)
                        funcao_decorada()  """


@calcula_duracao
def contador():
    for n in range(0, 100000):
        pass  # pass - é uma operação nula - quando é executado, nada acontece. É útil como um marcador quando uma
        # instrução é necessária sintaticamente, mas nenhum código precisa ser executado.

        # break - It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.
        # Coloquei a definição de break só pq lembrei


# Executa a função 'contador'
contador()

print("=" * 30)

""" Decorators with arguments """


def function1(function):
    def wrapper(*args, **kwargs):
        """
        Basicamente, ela aceita qualquer quantidade de parâmetros e qualquer quantidade de tipos de parâmetros:
            *arg = à quantidade de parâmetros do mesmo tipo. Ele é uma tuple (lista imutável), você está passando uma
            lista de informação ou seja, de tamanho indefinido, não é um ou dois é uma lista que pode ter quantos termos
            forem necessários.
            **kwarg = quantidade de tipos de parâmetros. Ele é um dict (key-value), você está passando
            um datatype que sem ordenação, seguindo a definição key:value.
        """

        print("Hello,")
        function(*args, **kwargs)
        print("Are you ok?")

    return wrapper


@function1
def function2(name, age):
    print(f"{name}, {age}")
    print("*arg e **kwarg aceitam qualquer coisa, um tanto de parâmetros de vários tipos, tipo string com int", 23+5)


function2("Abacaxi", 24)
