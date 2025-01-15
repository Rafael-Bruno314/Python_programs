import os
from pypdf import PdfWriter

pdf_de_entrada = "Apostila definitiva v.05 3x3.pdf" #O caminho/nome do pdf
paginas_a_isolar = [409] #É uma lista, coloque quantas quiser separadas por vírgula
nome_pdf_saida = "3x3.pdf" #O nome do pdf de saída

writer = PdfWriter()

paginas_a_isolar = [x - 1 for x in paginas_a_isolar]
writer.append(pdf_de_entrada, pages=paginas_a_isolar)

writer.write(nome_pdf_saida)
writer.close()