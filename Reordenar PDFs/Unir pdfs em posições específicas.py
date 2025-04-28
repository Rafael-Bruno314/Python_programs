from pypdf import PdfWriter

# Cria um objeto PdfWriter para mesclar PDFs
merger = PdfWriter()

# Adiciona o primeiro arquivo PDF (arquivo principal)
merger.append("Título")

# Mescla o segundo arquivo PDF em uma posição específica do primeiro
# position=1 indica que será inserido após a primeira página do arquivo principal
# fileobj especifica o arquivo a ser inserido
merger.merge(position=1, fileobj="Sumário.pdf")

# Gera o arquivo PDF de saída com o resultado da mesclagem
merger.write("output.pdf")

# Fecha o objeto merger
merger.close()