#pip install pypdf
import os
from pypdf import PdfWriter


# Configuração dos arquivos e páginas:

file_path = os.path.dirname(__file__)
file_name = "" # Adicione o nome do arquivo que queira extrair as páginas

pdf_de_entrada = f"{file_path}\\{file_name}"  # Caminho/nome do PDF original
paginas_a_isolar = [22]  # Lista das páginas para extrair (numeração começa em 1)
nome_pdf_saida = f"pag_{paginas_a_isolar}.pdf"  # Nome do arquivo de saída

if not os.path.exists(pdf_de_entrada):
    print(f"Erro: Arquivo '{pdf_de_entrada}' não encontrado!")
    exit()


# Inicializa o objeto PdfWriter para criar o novo PDF
writer = PdfWriter()

# Ajusta a numeração das páginas (Python usa índice 0, PDFs começam em 1)
paginas_a_isolar = [x - 1 for x in paginas_a_isolar]

# Adiciona as páginas selecionadas ao novo PDF
writer.append(pdf_de_entrada, pages=paginas_a_isolar)

# Salva o novo arquivo PDF
writer.write(nome_pdf_saida)

# Fecha o objeto writer para liberar recursos
writer.close()