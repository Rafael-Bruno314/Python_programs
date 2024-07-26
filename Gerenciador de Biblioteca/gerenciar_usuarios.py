from intermedio_db import *
import time

class Usuarios:


    def exibir_usuario():
        print("-"*30)
        print("usuários cadastrados:")
        print("-"*30)
        for indice, usuario in enumerate(usuarios_db(), start=1):
            print(f"{indice} - {usuario}\n")

    def pesquisar_usuario(user):
        temp_user = ""
        for indice, usuario in enumerate(usuarios_db()):
            if(usuario == user):
                temp_user = usuario
        if temp_user == "":
            print("Esse nome não foi encontrado na base de dados. Vamos cadastrá-lo")
            time.sleep(3)
            temp_user = cadastra_db(user,"usuarios.txt")
        return temp_user



