import os
import shutil
import time
from pypdf import PdfWriter

merger = PdfWriter()

nome_do_arquivo_apostila = "Apostila (quase) definitiva v.02.pdf"
nome_do_anexo = "Planejamento.pdf"


merger.append(nome_do_arquivo_apostila)
merger.merge(position=1857, fileobj=nome_do_anexo)


merger.write("output.pdf")
merger.close()
