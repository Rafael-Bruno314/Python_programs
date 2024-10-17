import os
import shutil
import time
from pypdf import PdfWriter

merger = PdfWriter()

nome_do_arquivo_apostila = "Apostila (quase) definitiva v.04 3x3.pdf"
nome_do_anexo = ""


merger.append("Capa de Livro Biologia Verde Branco e Preto.pdf")
merger.append("Sumário.pdf")
merger.append(nome_do_arquivo_apostila)
merger.append("Fundo.pdf")


"""
merger.append("Nome do arquivo.pdf", pages=(pag_inicial, pag_final))
merger.merge(position= a partir de qual página adicionar o anexo, fileobj="Nome do arquivo.pdf", pages=(pag_inicial, pag_final))
"""
"""
merger.append(nome_do_arquivo_apostila, pages=(0, 951))

merger.append("Capa - Fundamentos da Educação.pdf")
merger.append("Fund.pdf")
merger.append("Capa - Fund. da Educ. de Jovens e Adultos e Educ. Popular.pdf")
merger.append("EJA.pdf")

merger.append(nome_do_arquivo_apostila, pages=(1559, 4744))
"""

merger.write("output.pdf")
merger.close()
