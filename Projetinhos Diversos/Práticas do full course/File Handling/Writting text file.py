import os
print("a - append: will append to the end of the file")
print("w - Write: will overwrite any existing content")

file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'w')
file.write("Hello World\n")
file.write("Hello World again?")
file.close()

file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'w')
file.write("Oops overwritten")
file.close()

