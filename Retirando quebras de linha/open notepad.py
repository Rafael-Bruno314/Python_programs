import subprocess
import os

# Caminho do arquivo a ser aberto
diretorio = os.getcwd()
endereco = diretorio + "\\Retirando quebras de linha\\texto.txt"

# Comando para abrir o Bloco de Notas com um arquivo específico
subprocess.Popen(['notepad.exe', endereco])

