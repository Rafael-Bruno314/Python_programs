import random

print("While loop")

count = 0
while count < 9:
    print("Number: ", count)
    count += 1

print("Good bye")

print("="*30)

to_be_guessed = random.randrange(1, 20, 1)
guess = 0

"""
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:   # Esse else é do próprio while!! Não sabia que isso era possível.
    print("Congratulation, you made it!")
"""
print("="*30)

print("For loop")

print(list(range(1, 10)))   # Remembering that range 1 to 10 is equal 1, 2, ..., 8, 9.

num = 5
factorial = 1

if num < 0:
    print("Must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)

print("="*30)

print("Nested loops - loops inside loops")
# Nothing new...
