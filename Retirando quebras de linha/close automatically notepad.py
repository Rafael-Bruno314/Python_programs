import subprocess
import time
import os


# Caminho do arquivo a ser aberto
diretorio = os.getcwd()
caminho_arquivo = diretorio + "\\Retirando quebras de linha\\texto.txt"

# Abre o Bloco de Notas
notepad_process = subprocess.Popen(['notepad.exe', caminho_arquivo])

# Salva o timestamp inicial do arquivo
initial_timestamp = os.path.getmtime(caminho_arquivo)

print(initial_timestamp)

# Verifica se o arquivo foi modificado
def file_modified(path, initial_timestamp):
    try:
        return os.path.getmtime(caminho_arquivo) != initial_timestamp
    except FileNotFoundError:
        return False #Seria interessante criar o arquivo caso não exista

# Aguarda a modificação do arquivo
while not file_modified(caminho_arquivo, initial_timestamp):
    time.sleep(1)

subprocess.call('TASKKILL /F /IM notepad.exe')