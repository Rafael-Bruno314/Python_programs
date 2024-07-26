import json
import time

def livros_db() -> list:
    with open("livros.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_livros = json.loads(conteudo)
    return lista_de_livros


def cadastra_db(entrada:str, nome_db:str):
    with open(nome_db, "r+", encoding='utf-8',errors='ignore') as arquivo:
        db_antes = arquivo.read()
        db_antes = db_antes[:-1]
        arquivo.seek(0)
        arquivo.write(db_antes + "," + json.dumps(entrada, ensure_ascii=False) + "]")
    time.sleep(1)
    if __name__ == "gerenciar_livros":
        print(f"Livro '{entrada['nome']}' de {entrada['autor']} com ISBN {entrada['isbn']} adicionado com sucesso.")
    elif __name__ == "gerenciar_usuarios":
        print(f"Usuário {entrada} adicionado com sucesso!")
        return entrada


def atualiza_livro(novo_db:list):
    with open("livros.txt", "w", encoding='utf-8') as write_arquivo:
        write_arquivo.write(json.dumps(novo_db, ensure_ascii=False))


def usuarios_db() -> list:
    with open("usuarios.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_users = json.loads(conteudo)
    return lista_de_users