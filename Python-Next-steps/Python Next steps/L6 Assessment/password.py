correctPassword = "letMeIn"
attempts = 0
guess = ""
goAgain = True

while goAgain:                                  # Repeat as long as goAgain is True
    guess = input("Enter the password: ")       # Ask for a password
    if guess == correctPassword:                # If correct, print message and stop looping
        print("Correct, you are now logged in")
        goAgain = False
    else:                                       # If incorrect, increase 'attempts' counter
        print("Error, incorrect")
        attempts = attempts + 1
        if attempts == 3:                       # If 3 attempts, lock user out and stop looping
            print("3 incorrect attempts - this account is now locked")
            goAgain = False



