# Note: To keep it simple we are using answer as a string variable
# This way we don't have to convert the input to a number

answer = "8"
guess = input("Guess a number: ")
# Alternative line code if using numbers:
# guess = int(input("Guess a number: "))

while guess != answer:
    print("That's wrong, try again!")
    guess = input("Guess a number: ")

print("\nWell done, that's right!")

input("\nPress ENTER to exit program")
