import random
girl_babynames = ["Sarah","Willow","Danni","Amanda"]
boy_babynames = ["Frank","Will","Dave","Chris"]

print("Welcome to random baby name generator")
print("What would you like to do?")
choice = int(input("1.Choose a girls name? or 2.Choose a boys name"))
if choice ==1:
         print("you have chosen to choose a girls name")
         print("The computer has selceted:")
         print(random.choice(girl_babynames))
elif choice ==2:
         print("you have chosen to choose a boys name")
         print("The computer has selceted:")
         print(random.choice(boy_babynames))
else:
         print ("error please enter 1 or 2 only")
               
#tough - #Go through the code and comment each line
         #explaining what each piece of code does.
         
#tougher # Add a loop so the program will repeat.
         
#Toughest#Add another if statement and loop so
         #that if the user enters anything other than a 1 or a 2 it
         #will give an error and let them have
         #another go.

#ninja - # once you have compelted all of the above. Add another option 3. to add to the boys
         # names list and another option 4 to add to the girls names list.
         # Use the exampl code below to help :
         #        mylist = ["cake",Chocolate"]
         #        food = input("what would you like to add?")
         #        mylist.append(food)
         #        print(mylist) - This will check it worked! 
         
         

