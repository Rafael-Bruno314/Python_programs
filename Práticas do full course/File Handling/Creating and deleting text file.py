import os   # Is used to delete files
# Used this module always you handle with file is a good habit in programing

""" Creating file """

file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\newfile.txt', 'w')
# Can create with a, w and x. Note that x can be used with the file.write
file.write("This is a new file")
file.close()

""" Deleting file """
# Delete a file that doesn't exist cause an error, so...

if os.path.exists(r"C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\newfile.txt"):
    os.remove("newfile.txt")
    print("File removed")
else:
    print("The file doesn't exist")


""" Deleting a folder """

# os.rmdir("my folder")
