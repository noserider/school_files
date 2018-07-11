# SECTION 1
correctPassword = "pa55word"
guesses = 0
guess = ""


# SECTION 2
while guess != correctPassword:
    guess = input("Try to guess the password: ")
    guesses = guesses + 1

print("Password guessed correctly")


# SECTION 3
if guesses == 1:
    print("That took you 1 guess.")
else:
    print("That took you " + str(guesses) + " goes.")

input("\nPress ENTER to exit program")
