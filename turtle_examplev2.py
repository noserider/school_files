from appJar import gui
import tkinter
import turtle

app = gui("Molly ashcroft")

def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()

app.setSticky("news")
fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

canvas = tkinter.Canvas(app.topLevel, width=350, height=350)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
screen.tracer(100, 0)
t.hideturtle()
t.speed(0)
t.pencolor("blue")
t.home()
t.pd()
side = 23
angle =145

for _ in range(160):
    t.backward(side)
    t.left(angle)
    side += 4

screen.update()

app.go()
