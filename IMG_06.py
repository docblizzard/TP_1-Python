from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="white", height=900, width=900)

colors = ['royal blue', 'snow', 'SteelBlue4', 'light coral', 'sienna2', 'blue violet', 'sandy brown', 'plum3', 'PaleGreen1', 'DarkSlateGray1']

for x in range(0, 10, 1):
    w.create_rectangle((random.randint(180,720)), (random.randint(90,720)), 

(random.randint(90,720)),(random.randint(180,720)), (random.randint(90,720)))


w.pack()
root.mainloop()

## Raté
