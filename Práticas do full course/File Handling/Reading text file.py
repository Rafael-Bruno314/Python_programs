"""Example 1"""
import os
file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'r')
print(file.read())
file.close()

"""Example 2"""
import os
file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'r')
print(file.read(5))     # Just read the 5 firsts characters in text
file.close()

"""Read-line"""
import os
file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'r')
print(file.readline())     # Read the first line only
file.close()

import os
file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'r')
print(file.readlines())     # Read the lines separately
file.close()

"""Looping over a file object"""
import os
file = open(r'C:\Users\1234\Documents\Programação\Python\Práticas\File Handling\demofile.txt', 'r')
for line in file:
    print(file.readlines())     # Read the lines separately, except the first line
file.close()
