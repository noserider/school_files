life = 1

input ("Welcome to Mr W's Adventure game. \n Press Enter to Play")

q1= input("You wake up and find yourself at the foot of a large oak tree \n in a quite snow covered field. \n In the distance you can see a cave. \n What would you like to do? \n 1. Walk towards the cave \n 2. Climb the tree \n 3. Make a Fire \n 4. Go to sleep. \n :")

while life > 0:
    if q1 == "0":
        q1 = input("What would you like to do? \n 1. Walk towards the cave \n 2. Climb the tree \n 3. Make a Fire \n 4. Go to sleep.\n :")

    elif q1 == "1":
               print("1")
                   
    elif q1 == "2":
        print ("You picked 2, Climb the Tree")
        input ("You start to climb the tree, \n about half way to the top you hear the sound of breaking wood \n Press Enter to find out what happends when climb a large, dead tree")
        life = life - 1

    elif q1 == "3":
        print ("You picked 3, Make a Fire")
        print ("You do not have any wood or matches \n pick again")
        q1 = "0"
        
    elif q1 == "4":
        print ("You picked 4, Go to Sleep")
        input ("You fall asleep and become cold, \n Press Enter to see what happends when you fall asleep in the snow")
        life = life - 1

    else:
        print ("That was not an option.")
        q1 = "0"


print ("You DEAD!!!!")
