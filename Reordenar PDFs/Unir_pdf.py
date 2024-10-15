import os
from PyPDF2 import PdfMerger


# Caminho da pasta que contém os arquivos
caminho_pasta = 'C:\\Users\\Rafael Bruno\\Documents\\Formação Pedagógica\\PDFs das Disciplinas\\Planejamento Escolar e Avaliação da Aprendizagem'

# Lista para armazenar os nomes dos arquivos PDF
arquivos_pdf = []

# Itera sobre os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    # Verifica se o arquivo é um PDF
    if nome_arquivo.endswith('.pdf'):
        arquivos_pdf.append(nome_arquivo)

print(arquivos_pdf)

# Inicializa o objeto PdfMerger
unificador_pdf = PdfMerger()

for arquivo in arquivos_pdf:
    print(caminho_pasta+'\\'+arquivo)


# Adiciona todos os arquivos PDF para serem unidos
for arquivo in arquivos_pdf:
    unificador_pdf.append(caminho_pasta+'\\'+arquivo)

# Define o nome do arquivo PDF final unido
arquivo_pdf_unido = 'arquivo_unido.pdf'

# Escreve o arquivo PDF final
unificador_pdf.write(os.path.join(caminho_pasta, arquivo_pdf_unido))
unificador_pdf.close()

print(f'PDFs unidos com sucesso em: {os.path.join(caminho_pasta, arquivo_pdf_unido)}')
