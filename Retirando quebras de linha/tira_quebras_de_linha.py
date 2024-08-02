import os

diretorio = os.getcwd()
endereco = diretorio + "\\Retirando quebras de linha\\texto.txt"


with open (endereco, "r") as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.replace("\n", " ")

with open(endereco, "w") as arquivo:
    arquivo.write(conteudo)