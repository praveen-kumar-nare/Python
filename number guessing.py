import random

n = random.randrange(1, 10)
guess = int(input("Enter any number: "))

while n != guess:
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high!")
    guess = int(input("Enter number again: "))

print("You guessed it right!!")
