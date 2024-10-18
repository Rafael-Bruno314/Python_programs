from pypdf import PdfWriter

merger = PdfWriter()

merger.append("Apostila (quase) definitiva v.05 3x3.pdf")
merger.merge(position= 1, fileobj="Sumário - 3x3.pdf")


merger.write("output.pdf")
merger.close()