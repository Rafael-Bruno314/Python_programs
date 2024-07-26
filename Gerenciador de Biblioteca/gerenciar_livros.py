from intermedio_db import *
from gerenciar_usuarios import Usuarios

class Visualizar():

    def exibir_livros():
        print("-"*50)
        print("Listando os livros cadastrados na base de dados:")
        print("-"*50)
        for indice, livro in enumerate(livros_db(), start=1):
            print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n")

    def listar_emprestimos():
        print("-"*50)
        print("Listando todos os livros com empréstimo:")
        print("-"*50)
        for indice, livro in enumerate(livros_db(), start=1):
            if(livro.get("Emprestado por") != None):
                print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n Emprestado para: {livro['Emprestado por']}\n")

    def listar_disponibilidade():
        print("-"*50)
        print("Listando todos os livros disponíveis:")
        print("-"*50)
        for indice, livro in enumerate(livros_db(), start=1):
            if(livro.get("Emprestado por") == None):
                print(f"{indice} - Título: {livro['nome']} \n Autor: {livro['autor']} - ISBN: {livro['isbn']}\n")

    def procurar_livros(info:str) ->int:
        indice = []
        for key, livro in enumerate(livros_db()):
            for chave, valor in livro.items():
                if(info == valor):
                    indice.append(key)
        return indice[0]
    
    def buscar_livros(info):
        resultados = []
        for livro in livros_db():
            for chave, valor in livro.items():
                if(info == valor):
                    resultados.append(livro)
        print(f"Foram encontrados {len(resultados)} resultados para a busca:") if len(resultados)>1 else print(f"Foi encontrado {len(resultados)} resultado para a busca:")
        for resultado in resultados:
            print(f"Título: {resultado['nome']} \n Autor: {resultado['autor']} - ISBN: {resultado['isbn']}\n")


class Livros():   

    def adicionar_livro(titulo, autor, isbn):
        print("Adicionando novo livro")
        livro = json.dumps({"nome": titulo, "autor": autor, "isbn": isbn}, ensure_ascii=False)
        cadastra_db(livro,"livros.txt")
        print(f"Livro '{titulo}' de {autor} com ISBN {isbn} adicionado com sucesso.")

    def atualizar_livro(info:str):
        indice = Visualizar.procurar_livros(info)
        print("Qual dado deseja atualizar? ", end=" ")
        dado = input()
        print("Qual o novo valor? ", end=" ")
        valor = input()   
        nova_lista = livros_db()
        nova_lista[indice][dado] = valor
        atualiza_livro(nova_lista)
        print(f" Livro atualizado com sucesso para {nova_lista[indice][dado]}")
        

    def excluir_livro(info: str):
        indice = Visualizar.procurar_livros(info)
        nova_lista = livros_db()
        nova_lista.pop(indice)
        atualiza_livro(nova_lista)
        print("Livro Removido")


class Biblioteca:

    def emprestar_livro(usuario):
        print("Empréstimo de um livro")
        Visualizar.listar_disponibilidade()     
        print("Qual livro deseja pegar emprestado?", end=" ")
        info = input()
        if(info.isdigit() and int(info) <= 999):
            indice = int(info, base=10)-1
        else:
            indice = Visualizar.procurar_livros(info)     
        nova_lista = livros_db()
        nova_lista[indice]["Emprestado por"] = usuario
        atualiza_livro(nova_lista)
        print(f"Livro {livros_db()[indice]['nome']} emprestado para {usuario}")

    def devolver_livro():
        Visualizar.listar_emprestimos()
        print("Qual livro deseja devolver (Digite o índice)?")
        indice = int(input())-1
        nova_lista = livros_db()
        del nova_lista[indice]["Emprestado por"]
        atualiza_livro(nova_lista)
        print(f"O livro {livros_db()[indice]['nome']} de {livros_db()[indice]['autor']} foi devolvido com sucesso!")
