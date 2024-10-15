import os
from pypdf import PdfMerger
import time

merger = PdfMerger(strict=False)
#caminho_pasta = "C:\\Users\\Rafael Bruno\\Downloads"
caminho_pasta = "C:\\Users\\Rafael Bruno\\Documents\\Formação Pedagógica\\PDFs das Disciplinas\\Fund. da Educ. de Jovens e Adultos e Educ. Popular4"
caminho_destino = os.getcwd()


# Itera sobre os arquivos na pasta de origem
for raiz, diretorios, arquivos in os.walk(caminho_pasta):
    for arquivo in arquivos:     
    # Verifica se o arquivo é um PDF
        if arquivo.endswith('.pdf'):
            try:
                caminho_completo_origem = os.path.join(raiz, arquivo)
                merger.append(fileobj=caminho_completo_origem)
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")


time.sleep(3)

merger.write("output.pdf")
merger.close()