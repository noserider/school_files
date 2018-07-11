# Task 1

heroes = ["Batman","Wonder Woman","Superman","Spiderman"]

# Task 2

print("Current pilot:",heroes[0])

# Task 3

print("Co-pilot:",heroes[1])

# Task 4

heroes[2] = "Hit Girl"

# Task 5

heroes.append("Wolverine")
heroes.append("Iron Man")

# Task 6

print()
print("The Super Hero Alliance!")
print(heroes[0])
print(heroes[1])
print(heroes[2])
print(heroes[3])
print(heroes[4])
print("and")
print(heroes[5])
print()

# Task 6 Alternative

print(heroes)

# Possible Extension Response

print()
print("Which team member would you like to replace (0-5)")
choice = int(input())
print("Which superhero will be joining the team?")
newHero = input()

heroes[choice] = newHero

print()
print("The NEW Super Hero Alliance!")
print(heroes[0])
print(heroes[1])
print(heroes[2])
print(heroes[3])
print(heroes[4])
print("and")
print(heroes[5])
print()
