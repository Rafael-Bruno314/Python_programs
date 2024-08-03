import subprocess
import time
import os

# Caminho do arquivo a ser aberto
diretorio = os.getcwd()
caminho = os.path.join(diretorio, 'texto.txt')

#Abre ou cria e abre o texto.txt
if os.path.exists(caminho):
    subprocess.Popen(['notepad.exe', caminho])
else:
    with open(caminho, 'w') as arquivo:
        arquivo.close()
    subprocess.Popen(['notepad.exe', caminho])

# Salva o timestamp inicial do arquivo
initial_timestamp = os.path.getmtime(caminho)

while True:
    if(os.path.getmtime(caminho) != initial_timestamp):
        # Verifica se o arquivo foi modificado
        break
    time.sleep(1)

subprocess.call('TASKKILL /F /IM notepad.exe')

with open (caminho, "r") as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.replace("\n", " ")

with open(caminho, "w") as arquivo:
    arquivo.write(conteudo)

subprocess.Popen(['notepad.exe', caminho])