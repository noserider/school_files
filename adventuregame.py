life = 1

input ("Welcome to Mr W's Adventure game. \n Press Enter to Play")

q1= input("You wake up and find yourself at the foot of a large oak tree \n in a quite snow covered field. \n In the distance you can see a cave. \n What would you like to do? \n 1. Walk towards the cave \n 2. Climb the tree \n 3. Make a Fire \n 4. Go to sleep. \n :")

while life > 0:
    if q1 == "0":
        q1 = input("What would you like to do? \n 1. Walk towards the cave \n 2. Climb the tree \n 3. Make a Fire \n 4. Go to sleep.\n :")

    elif q1 == "1":
        print ("You picked 1. Walk towards the cave")
        q2 = input ("After a walk through the thick snow, you reach the cave \n Outside the cave you see a Storage chest \n What would you like to do? \n 1. Walk back to the tree \n 2. Enter the cave \n 3. Open the chest \n 4. Climb above the cave \n :")
        if q2 == "0":
            q2 = input ("What would you like to do? \n 1. Walk back to the tree \n 2. Enter the cave \n 3. Open the chest \n 4. Climb above the cave \n :")
            
        elif q2 == "1":
            print ("You picked 1. Walk back to the tree")
            q1 = "0"
                
        elif q2 == "2":
            print ("You picked 2. Enter the cave")
            input ("You enter the cave and find yourself in the pitch black. \n You start stumbling around the cave by feeling the walls. \n Press enter to find out what happends when you walk around a cave in the dark")
            life = life - 1
        elif q2 == "3":
            print ("You picked 3. Open the chest")
            q3 = input ("In the chest you find a warm jacket, a torch and a gold key. \n What would you like to do? \n 1/. \n 2. \n 3. \n 4. \n ")
                
        elif q2 == "4":
            print ("You picked 4. Climb above the cave")
            input ("You start using your spider like skills to climb the rock face. \n Press enter to find out what happends when you climb an ice covered rock face")
            life = life - 1
                
                   
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
