import tkinter as tk
root = tk.Tk()

g = tk.Canvas()
g.pack()

r = 5
y = 15
colors = ['red', 'green', 'blue']

for i in range (1,15):
    print(i)
    x = 30
    for j in range(1,i):
        if i < 5:
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[0])
        elif 4 < i < 9:
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[1])
        else:
            g.create_oval(x-r, y-r, x+r, y+r, fill=colors[2])
        x += 2 + r
    y += 2 +r
root.mainloop()
