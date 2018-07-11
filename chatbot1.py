import time
import random

name = input("Hello, what is your name?")

time.sleep(2)
print ("Hello",name)

feeling = input("how are you today? ")

time.sleep(2)
if "good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")
