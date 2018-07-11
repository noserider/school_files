#import the library
from appJar import gui
import random

# a list of possible answers - you can place your own here
answers = ["Can't tell you now", "It is certain", "Ask again later", "Yes", " Don't count on it", "Doubtful", "No chance"]

win = gui("Magic 8-Ball")
win.setResizable(False)
win.setFont(18)

def clear(btn):
    win.clearEntry("Question")
    win.clearLabel("Answer")

# function to deal with button press
def shake (btn):
    if len (win.getEntry ("Question")) == 0:
        win.errorBox ( "Error", "You must ask a question" )
    else:
        answer = random.choice(answers)
        win.setLabel("Answer",answer)



win.addEntry("Question")
win.addButtons(["Shake","Clear"],[shake,clear])
win.addImage("8ball", "8ball.gif")
win.addEmptyLabel("Answer")
win.setLabelBg("Answer", "yellow")
win.setFocus("Question")

#start the gui
win.go()




   
