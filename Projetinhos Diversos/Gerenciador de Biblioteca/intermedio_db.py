import json
import time
import os

dir_atual = os.path.dirname(__file__)
db_path = os.path.join(dir_atual, 'livros.txt')
user_path = os.path.join(dir_atual, 'usuarios.txt')

def livros_db() -> list:
    with open(db_path, "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_livros = json.loads(conteudo)
    return lista_de_livros

def cadastra_user(user:str):
    with open(user_path, "r+", encoding='utf-8',errors='ignore') as arquivo:
        db_antes = arquivo.read()
        db_antes = db_antes[:-1]
        arquivo.seek(0)
        arquivo.write(db_antes + "," + json.dumps(user, ensure_ascii=False) + "]")
    time.sleep(1)
    print(f"Usuário {user} adicionado com sucesso!")
    return user

def cadastra_livro(livro:str):
        with open(db_path, "r+", encoding='utf-8',errors='ignore') as arquivo:
            db_antes = arquivo.read()
            db_antes = db_antes[:-1]
            arquivo.seek(0)
            arquivo.write(db_antes + "," + livro + "]")
        time.sleep(1)

def atualiza_livro(novo_db:list):
    with open(db_path, "w", encoding='utf-8') as write_arquivo:
        write_arquivo.write(json.dumps(novo_db, ensure_ascii=False))


def usuarios_db() -> list:
    with open(user_path, "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_users = json.loads(conteudo)
    return lista_de_users