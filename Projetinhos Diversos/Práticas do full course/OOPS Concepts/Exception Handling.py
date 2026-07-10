"""

*raise* allows you to throw an exception at any time

*assert* enables you to verify if a certain condition is met and throw an exception if it isn't

In the *try* clause, all statements are executed until an exception is encountered

*except* is used to catch and handle the exception(s) that are encountered in *try* clause

*else* lets you code sections that should run only when no exceptions are encountered in the *try* clause

*finally* enables you to execute sections of code that should always run, with or without any previosly encountered
exceptions

"""

""" 
Estrutura de um exception handlind completo 

try:
    {Run this code}
except:
    {Execute this code when there is an exception}
else:
    {No exceptions? Run this code}
finally:
    {Always run this code}

"""

""" Some examples """

# raise
x = 10
if x == 10:
    # raise Exception("x não deveria ser 10!")    # Sai um erro personalizado da minha escolha, mesmo que isso não seja
    # um erro de verdade, da lógica ou da sintaxe, é apenas um erro porque eu quis
    pass  # Só pra passar o if já que eu vou dar comment no raise

# assert (afirmar)
import sys


# assert ('linux' in sys.platform), "This code runs on Linux only"
# Basicamente cria um erro se sua condição for falsa e exibe algo. É uma forma de parar um programa no começo para
# evitar erros inesperados no meio dele, já que eles, em teoria, seriam esperados

# try and except block


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems"
    print("Doing something")


try:
    linux_interaction()
except AssertionError as error:  # Pode-se colocar uma mensagem para cada tipo de erro específico. Existem
    # milhares de exceptions, mas eles aparecem quando o programa crasha pra vc saber com qual lidar!
    print(error)
    print('The linux_interaction() function was not executed')
except:
    print("Linux function was not executed")  # Vai rodar a função, gerar um AssertionError ao invés de exibir a
    # mensagem vai cair no except e executar o que tiver nele. E assim o programa não vai crashar.

# Pode-se ter vários excepts em um built-in exception

print("=" * 30)

""" Built-in exceptions to open a file """

try:
    # with open('file.log') as file:
    with open(r"C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt") as file:
        # O with é usado para garantir finalização de recursos adquiridos. Ele consegue manipular objetos que contenham
        # os métodos __enter__() e __exit__(). Eles são chamados internamente logo no início da execução do bloco criado
        # e dentro do finally interno criado no bloco
        read_data = file.read()
        """
        Essa função acima é o mesmo que:
            try:
                __enter__()
                open("my_file.txt") as file:
                    data = file.read()
                    #faça algo com "data"
            finally:
                __exit__()
        """
except FileNotFoundError:
    print("Could not open file.log")
    print(FileNotFoundError)
else:
    print(read_data)    # Executa porque o demofile.txt existe
finally:
    print("Este código vai ser executado de qualquer jeito")
