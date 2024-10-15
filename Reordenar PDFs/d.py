import os
import subprocess
from PyPDF2 import PdfWriter

merger = PdfWriter()
caminho_pasta = 'C:\\Users\Rafael Bruno\\Documents\Formação Pedagógica\\PDFs das Disciplinas\\Planejamento Escolar e Avaliação da Aprendizagem'
arquivos_pdf = []
"""
for nome_arquivo in os.listdir(caminho_pasta):
    # Verifica se o arquivo é um PDF
    if nome_arquivo.endswith('.pdf'):
        arquivos_pdf.append(caminho_pasta+'\\'+nome_arquivo)


print(arquivos_pdf)

for arquivo in arquivos_pdf:
    #caminho_completo = os.path.join(caminho_pasta, arquivo)
    # O subprocess é usado para abrir os arquivos PDF
    subprocess.Popen([arquivo], shell=True)
"""

for nome_arquivo in os.listdir():
    # Verifica se o arquivo é um PDF
    if nome_arquivo.endswith('.pdf'):
        arquivos_pdf.append(nome_arquivo)

print(arquivos_pdf)

for pdf in arquivos_pdf:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()