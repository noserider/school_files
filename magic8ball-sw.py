from appJar import gui
import random

answers = ["Can't tell you now", "Go Away", "It is certain", "Ask again later"]

win = gui("Magic 8-Ball")
win.setResizable(False)
win.setFont(22)

def clear(btn):
    win.clearEntry("Question")
    win.clearLabel("Answer")

def shake(btn):
    if len(win.getEntry("Question")) == 0:
        win.errorBox("Error","You must ask a question")
    else:
        answer = random.choice(answers)
        win.setLabel("Answer",answer)

win.addEntry("Question")
win.addButtons(["Shake","Clear"],[shake,clear])
win.addImage("8ball","8ball.gif")
win.addEmptyLabel("Answer")
win.setLabelBg("Answer","yellow")
win.setFocus("Question")
win.go()
