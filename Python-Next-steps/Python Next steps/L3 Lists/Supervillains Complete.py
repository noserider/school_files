# Task 1

villains = ["The Joker","Magneto","Red Mist","Doc Ock"]

# Task 2

for counter in range(4):
    print(villains[counter])

# Task 3

wages = [21,17,3,5]

# Task 4

for counter in range(4):
    print(villains[counter],": £",wages[counter],"million")

# Task 5

totalWage = 0

for counter in range(4):
    totalWage = totalWage + wages[counter]            

print("Total wage bill: £",totalWage,"million")
