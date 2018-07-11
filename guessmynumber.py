import random

print("Guess the Number Game!")
print("**********************\n")
print("I am thinking of a number between 1 and 100.")
print("Try to guess what it is in as few attempts as possible.\n")

number = random.randint(1, 100)
guess = int(input("What is your first guess? "))
attempts = 1

while guess != number:
    if guess > number:
        print("Too high.")
    else:
        print("Too low.")
    guess = int(input("Guess again...: "))
    attempts = attempts + 1

print("Well done! You took",attempts,"attempts to guess it was number",number,)

