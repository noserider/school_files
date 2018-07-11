piggyBank = 0
goAgain = "yes"

while goAgain == "yes":
    amount = input("How much did you put in your piggy bank? ")
    piggyBank = piggyBank + float(amount)

    print("Your piggy bank now holds £" + str(piggyBank))

    goAgain = input("Would you like to go again? (y/n)")

    if goAgain == "y":
        goAgain = "yes"
    elif goAgain == "Y":
        goAgain = "yes"

print("Goodbye!")

input("\nPress ENTER to exit program")
