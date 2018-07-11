choice = input("Would you like an (I)nsult or a (C)ompliment? ")

# Simple Solution
if choice == "I":
    print("You smell funny")
else:
    print("You look lovely today")

# Medium Solution
if choice == "I":
    print("You smell funny")
elif choice == "C":
    print("You look lovely today")
else:
    print("Invalid response")

# Complete Solution 1
if choice == "I":
    print("You smell funny")
elif choice == "i":
    print("You smell funny")
elif choice == "C":
    print("You look lovely today")
elif choice == "c":
    print("You look lovely today")
else:
    print("Invalid response")

# Complete Solution 2
if choice == "I" or choice == "i":
    print("You smell funny")
elif choice == "C" or choice == "c":
    print("You look lovely today")
else:
    print("Invalid response")

# Complete Solution 3
# Adding ".upper()" will check the upper case version of choice
if choice.upper() == "I":
    print("You smell funny")
elif choice.upper() == "C":
    print("You look lovely today")
else:
    print("Invalid response")
