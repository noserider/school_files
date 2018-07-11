needed = 20
inPiggyBank = 10.50

extra = float(input("How much extra money do you have? "))

total = inPiggyBank + extra

if total >= needed:
    print("We have enough :-D")
else:
    print("Sorry, we need more :-(")

input("\nPress ENTER to exit program")
