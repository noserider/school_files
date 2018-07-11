 

# This is another example of a procedure
# The data that is passed into the brackets works
# a bit like a variable, but is called a parameter

def raspberryTalk(text): # This will output your text
    print (text)


# Introduction to program
raspberryTalk("Hello from the Raspberry Pi chat bot")
time.sleep(0.2)
raspberryTalk("I was created to get students interested in coding so I am very basic")
time.sleep(0.2)
raspberryTalk("But I have a great voice!")
time.sleep(0.3)
raspberryTalk("What is your name")
say = input("What is your name? ")

raspberryTalk("Hello and welcome" + say)


# Cheese Question
raspberryTalk("Do you like cheese?")

cheese = input("Do you like cheese, yes or no ").lower()

if cheese == "no":
    raspberryTalk("Me too, I hate cheese as well")
else:
    raspberryTalk("Yuk, that is so wrong")




