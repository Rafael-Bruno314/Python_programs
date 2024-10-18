import os
from pypdf import PdfWriter

merger = PdfWriter()

"""Variáveis que podem ser úteis"""
#caminho_raiz = "C:\\Users\\Rafael Bruno\\Documents\\Formação Pedagógica\\PDFs das Disciplinas\\"
#pasta_disciplina = "17-Geometria Espacial"
#caminho_pasta = caminho_raiz+pasta_disciplina
#caminho_destino = os.getcwd()
#nome_arquivo = caminho_pasta[caminho_pasta.rfind("\\")+1:]


for raiz, diretorios, arquivos in os.walk("."):
    for arquivo in arquivos:
    # Verifica se o arquivo é um PDF
        if arquivo.endswith('.pdf'):
            try:
                caminho_completo_origem = os.path.join(raiz, arquivo)
                #print(caminho_completo_origem)
                merger.append(fileobj=caminho_completo_origem)
                
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")

"""
merger.append("Nome do arquivo.pdf", pages=(pag_inicial, pag_final))
merger.merge(position= a partir de qual página adicionar o anexo, fileobj="Nome do arquivo.pdf", pages=(pag_inicial, pag_final))
"""

#merger.write(nome_arquivo+".pdf")
merger.write("output.pdf")
merger.close()