import os
import shutil
from pypdf import PdfMerger
import time

merger = PdfMerger(strict=False)
#caminho_pasta = "C:\\Users\\Rafael Bruno\\Downloads"
caminho_pasta = "C:\\Users\\Rafael Bruno\\Documents\\Formação Pedagógica\\PDFs das Disciplinas\\Planejamento Escolar e Avaliação da Aprendizagem7"
caminho_destino = os.getcwd()

def mover_arquivo(caminho_pasta, caminho_destino):
    # Itera sobre os arquivos na pasta de origem
    for nome_arquivo in os.listdir(caminho_pasta):
        # Verifica se o arquivo é um PDF
        if nome_arquivo.endswith('.pdf'):
            caminho_completo_origem = os.path.join(caminho_pasta, nome_arquivo)
            caminho_completo_destino = os.path.join(caminho_destino, nome_arquivo)
            
            # Move o arquivo PDF para a pasta de destino
            shutil.move(caminho_completo_origem, caminho_completo_destino)
            

mover_arquivo(caminho_pasta, caminho_destino)
time.sleep(3)

for file in os.listdir():
    if file.endswith(".pdf"):
        try:
            merger.append(file)
        except Exception as e:
            mover_arquivo(caminho_destino, caminho_pasta)
            print(f"Erro ao processar o arquivo {file}: {e}")

merger.write("output.pdf")
merger.close()

#Devolvendo os arquivos pra pasta original (mais o output.pdf)
mover_arquivo(caminho_destino, caminho_pasta)