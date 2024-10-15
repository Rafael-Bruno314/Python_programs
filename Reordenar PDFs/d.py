import os
from pypdf import PdfMerger, PdfWriter

merger = PdfWriter()

for file in os.listdir():
    if file.endswith(".pdf"):
        try:
            merger.append(file)
        except TypeError as e:
            #mover_arquivo(caminho_destino, caminho_pasta)
            print(f"Erro ao processar o arquivo {file}: {e}")

merger.write("output.pdf")
merger.close()