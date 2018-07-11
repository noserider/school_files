from microbit import *
import random

rock = Image("00000:00900:09990:99999:99999")
paper = Image("00000:00000:99999:00000:00000")
scissors = Image("90009:09090:00900:09990:99999")

rps = [rock, paper, scissors]

while True:
    if accelerometer.was_gesture("shake"):
        display.show(random.choice(rps))
        