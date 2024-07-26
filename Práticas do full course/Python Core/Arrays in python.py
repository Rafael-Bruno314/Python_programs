# There are three ways to import arrays:

# import array
import array as arr  # method with alias (same thing (array) but I call by a different name (arr)

# to be more easy to handle) and this will be used
# from array import *     # This way I don't need to declare that it's a module

# Arrays are just like a lists but they can only support one datatype while lists can have any datatype
# Therefore, there are some operations with arrays (same datatype) which don't have with lists with different datatype.

print("Adding elements to an array")

a = arr.array('d', [1.1, 2.1, 3.1])
a.append(3.4)
print(("Array a = ", a))

b = arr.array('d', [1.1, 2.1, 3.1])
b.extend([4.5, 3.6, 7.2])
print(("Array b = ", b))

c = arr.array('d', [1.1, 2.1, 3.1])
c.insert(2, 3.4)
print("Array c = ", c)

print("=" * 30)

print("Removing elements of an Array")

a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7])
print("Popping last element:", a.pop())
print(a)
print("Popping fourth element:", a.pop(3))  # Remove the value in this position, don't matter what it is
print(a)

a.remove(1.1)  # Remove the value 1.1 independent of your position
print(a)

print("=" * 30)

print("Array Concatenation")

a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
b = arr.array('d', [3.7, 8.6])

c = a + b
print(type(c))  # c is an array
print("Array c = ", c)

print("=" * 30)

print("Slicing an array")

a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
print(a[0:3])
print(a[-3::])  # Pegando os últimos 3 valores do array

print("=" * 30)

print("Looping through an array")

# With for:
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
print("All values")

for x in a:
    print(x)

print("="*12)

# With while:
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
b = 0

while b < len(a):
    print(a[b])
    b = b + 1
