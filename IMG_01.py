from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="lightgray", height=900, width=900)

for j in range(30):
    for i in range(30):
        if (i % 2) != (j % 2):
            w.create_rectangle(i * 30, j * 30, (i + 1) * 30, (j + 1) * 30, fill="darkgrey", width=0)

w.create_rectangle(0, 0, 400, 400, fill="red", width=0)


for x in range(0, 120):
    w.create_line(random.randint(0, 900), random.randint(0, 900), random.randint(0, 900), random.randint(0, 900), width = 4)


w.pack()
root.mainloop()

# create_line( x0, y0, x1, y1)