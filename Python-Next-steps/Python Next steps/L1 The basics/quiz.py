score = 0


print("What kind of animal is a Python?")
print("A. A dog")
print("B. A fish")
print("C. A snake")
print("D. A bird")
choice = input("Type in a letter to guess: ")

if choice == "C" or choice == "c":
    print("Well done, that's right!")
    score = score + 1
else:
    print("Wrong, wrong, wrong!")

print("\n") # Blank lines ("\n" means "new line")

print("Which subject is NOT usually taught in schools?")
print("A. Maths")
print("B. Train spotting")
print("C. English")
print("D. Computing")
choice = input("Type in a letter to guess: ")

if choice == "B" or choice == "b":
    print("Well done, that's right!")
    score = score + 1
else:
    print("Wrong, wrong, wrong!")

print("\n")

print("The end! You scored " + str(score))

input("\nPress ENTER to exit program")
