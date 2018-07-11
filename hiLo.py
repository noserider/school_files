def getARandomNumber():
    import random
    number = random.randint(1,100)
    return number


# MAIN PROGRAM

target = getARandomNumber()
guess = int(input("Guess the random number: "))
while guess != target:
    if guess > target:
        guess = int(input("Too high, guess lower! "))
    else:
        guess = int(input("Too low, guess higher! "))
print("Well done!")
