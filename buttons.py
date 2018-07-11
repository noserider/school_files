from microbit import *

faces = [Image.HEART,Image.SAD,Image.CONFUSED]
faces2 = [Image.MEH,Image.COW,Image.PACMAN]

while True:
    if button_a.is_pressed:
        display.show(faces, loop=True, delay=1000)
    elif button_b.is_pressed:
        display.show(faces2, loop=True, delay=1000)