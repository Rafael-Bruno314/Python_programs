from PyPDF2 import PdfWriter

merger = PdfWriter()

apostila = "C:\\Users\\Rafael Bruno\\Documents\\Formação Pedagógica\\PDFs das Disciplinas\\Apostila definitiva\\Apostila (quase) definitiva v.01.pdf"
geometria = "C:\\Users\\Rafael Bruno\\Downloads\\Aula 02 Ângulos.pdf"
tendencias = "C:\\Users\\Rafael Bruno\\Downloads\\Tendências Pedagógicas.pdf"


input1 = open(geometria, "rb")
input2 = open(tendencias, "rb")


# add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 3))

# append entire input3 document to the end of the output document
#merger.append(input3)


# insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))



# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()






