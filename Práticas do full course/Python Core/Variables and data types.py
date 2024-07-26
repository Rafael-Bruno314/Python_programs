print("Data types:")
print("numbers")
print("string")
print("list")
print("dictionary")
print("tuple")
print("set")

# Numbers:

x = 10  # integer
print(type(x))

y = 10.234  # float
print(type(y))

z = 25j  # complex
print(type(z))

num = 10 > 9  # bool
print(type(num))

print("=" * 30)
# Strings:

a = 'hello'

b = "world"

print("Here is an example", a, b)

name = "Banana"
print(len(name))

print(name[2])  # Starts in zero

# name[2] = 'd'       # This is an error
# Strings are immutable. You can't change than without a function

print(name[2:8])  # Return of banana - nana

print(name[2:4])  # Return of banana - na

print(name[-2])  # Return the penultimate letter

print(name.upper())  # Return BANANA

print(name.lower())  # Return banana

print("=" * 30)
# Lists: ordered collection of values that can be changed. Duplicate entries are present.

mylist = [10, 20, 30, 30, 'banana', 'gold']
print(type(mylist))

print(mylist[2:5])  # Return 30, 30, 'banana'

mylist.append(10)  # Add 10 in the end of the list
print(mylist)

mylist.insert(5, 100)  # Add 100 between banana and gold
print(mylist)

mylist.reverse()  # Reverse the list
print(mylist)

print("=" * 30)
# Dictionary: like a list, but unordered collection os values that can be changed. NO duplicate entries are present.

courses = {1: 'python',
           2: 'javascript',
           'third': 'biotechnology'}
print(courses)

# Search terms from their keys (dictionary is a key-value relationship)
print(courses['third'], courses[1])     # Esse [1] é a key '1', se fosse por ordem o 'python' estaria na posição 0,
# o que não faz sentido em um dicionário onde não há ordem, primeiro termo, último ... não faz sentido pra ele,
# ele é só uma coleção de key-values sem sentido de ordem de aparição

print(courses.get('third'))  # Another form to get a term of dictionary

courses['four'] = 'English'  # Add a new value
print(courses)

print("=" * 30)
# Tuple: ordered and unchangeable. Immutable just like a string. We can have duplicate like in lists
# Ou seja, basicamente uma lista imutável

animals = (10, 10, 20, 'tiger', 'lion', 'giraffe', 'tiger')

print(type(animals))

print(animals)

print(animals[4])  # Shows 'lion'

print(animals.count('tiger'))  # Count the quantity of equals terms in a tuple

print("=" * 30)
# Set: A unordered collection with no duplicate entries allowed
# Sets are typically used with union, intersection, and difference math operations.

myset = {10, 20, 30, 40, 40, "lion", "monkey", "snake"}
print(type(myset))
print(myset)    # There won't be two '40', just one.
# O conjunto (set) é impresso em uma ordem aleatória, o que faz sentido já que ele é um datatype desordenado

# print(myset[2])     # This doesn't work, because a set doesn't allow indexes. Não faz sentido, não tem ordem de vdd

print("=" * 30)
# You can create variables with multiples types of data

a = [1, 2, 3, 4]     # list
b = {4, 5, 6, 4, 6}  # set (4 and 6 won't be repeated)

print(type(a), type(b))

c = [a, b]
print(c)

print("=" * 30)
# Range (intervalo): returns a number series in the range sent as an argument
# There are up to three parameters: start, stop (first), step

print(range(10))    # return "range(0, 10)"

print(list(range(10)))  # return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 10, 2)))    # Starts in 2 until 10 with 2 by 2 step
