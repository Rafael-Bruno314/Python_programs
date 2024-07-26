import sys
import time
from gerenciar_livros import *
from gerenciar_usuarios import Usuarios

def interface(retorno):
    if(retorno == 0):
        print("-"*50)
        print("Bem vindo ao gerenciador de bibliotecas!")
        print("-"*50)
        
        print("Cadastro de Livros")
        print("1 - Adicionar novo livro")
        print("2 - Remover livro existente")
        print("3 - Atualizar informações de um livro")
        print("4 - Listar todos os livros disponíveis")
        print("-"*50)
        print("5 - Registrar o empréstimo de um livro")
        print("6 - Registrar a devolução de um livro")
        print("7 - Listar todos os empréstimos ativos")
        print("-"*50)
        print("Consulta de Livros")
        print("8 - Procurar livro por título, autor ou ISBN")
        print("9 - Ver todos os livros disponíveis para empréstimo")
        print("0 - Sair")

        escolha_do_usuario = input("O que você deseja fazer?")
    else:
        escolha_do_usuario = input("O que mais você deseja fazer?")

    if(escolha_do_usuario == "1"):
        titulo = input("Qual o nome do livro?")
        autor = input("Qual o autor do livro?")
        isbn = input("Qual o ISBN do livro?")
        Livros.adicionar_livro(titulo, autor, isbn)
        interface(1)

    elif(escolha_do_usuario == "2"):
        info = input("Qual livro deseja Remover?")
        Livros.excluir_livro(info)
        interface(1)

    elif(escolha_do_usuario == "3"):
        info = input("Qual livro deseja atualizar?")
        Livros.atualizar_livro(info)
        interface(1) 
    
    elif(escolha_do_usuario == "4"):
        Visualizar.exibir_livros()
        interface(1)
    
    elif(escolha_do_usuario == "5"):
        print("possui cadastro? (s/n)", end=" ")
        cadastro = input()
        while cadastro != "s" or cadastro != "n":
            if(cadastro == "n"):
                print("Qual seu nome? ", end=" ")
                nome = input()
                Biblioteca.emprestar_livro(cadastra_db(nome,"usuarios.txt"))
                break
            else:
                usuario = input("Digite seu nome de usuário:")
                Biblioteca.emprestar_livro(Usuarios.pesquisar_usuario(usuario))
                break
        interface(1)

    elif(escolha_do_usuario == "6"):
        Biblioteca.devolver_livro()
        interface(1)
    
    elif(escolha_do_usuario == "7"):
        Visualizar.listar_emprestimos()
        interface(1)

    elif(escolha_do_usuario == "8"):
        info = input("Digite alguma informação do livro desejado:")
        Visualizar.buscar_livros(info)
        interface(1)

    elif(escolha_do_usuario == "9"):
        Visualizar.listar_disponibilidade()
        interface(1)

    elif(escolha_do_usuario == "0"):
        print("Saindo do programa...")
        time.sleep(3)
        sys.exit()

    else:
        print("Valor digitado inválido. Digite um valor válido")
        interface(0)

interface(0)