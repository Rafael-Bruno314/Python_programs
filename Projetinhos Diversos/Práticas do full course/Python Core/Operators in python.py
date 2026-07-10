print("Types of operators:")
print("Arithmetic:")

x = 10
y = 20

print(x + y, x - y, x * y, x / y)
print(x ** y)  # x power to y
print(x // y)  # x / y but just the integers, just quotient without rest
print(x % y)  # the rest of the division x by y

print("Assignment")

print("Used by assign (atribuir) values")
# x += 10 is equal to x = x + 10
# and other examples

print("Comparison")

print("==, !=, >, <, >=, <=")

print("Logical")

print("Logical operators are used to combine conditional statements")
print("AND, OR, NOT")

val = 10
num1 = 100
num2 = 1000

if val == num1 and num2 == num1:
    print("equal")
elif val > num1 or num2 > num1:
    print("greater")
else:
    print("smaller")

print(12 > 10)
print(12 < 10)
print(10 == 10)

print(not (12 > 10))  # It would be true but the not says the opposite

print("Identity")

print("is - Returns true if both variable are same object")
print("is not - Returns true if both variable aren't same object")

list1 = [10, 20, 30]
list2 = [10, 20, 30]

print(list1 is list2)   # Returns false
print(list1 == list2)   # Returns true because they have same values
print(list1 is not list2)   # Returns true

print("Membership operators")
print("Used to check if a sequence is present in an object")

print("in - Returns true if a sequence with the specified value is present in the object")
print("not in - Returns true if a sequence with the specified value isn't present in the object")

x = 10
print(x in list1)       # Returns true
print(list1 in list2)       # Returns false because they are lists

print("Bitwise")
print("used to compare binary numbers")
print("& (and), | (or), ^ (xor), ~ (not), << (left shift), << (right shift)")
