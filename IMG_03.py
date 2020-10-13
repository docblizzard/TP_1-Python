from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="white", height=900, width=900)
color = 16
color2 = 16
color3 = 16

for x in range (1, 800, 25):
    w.create_rectangle(25 + x, 25, 50 + x, 50, fill =  "#" + format(color, 'x') + "0000", width = "0" )
    color = color + 7


for y in range(1,400, 15):
    w.create_rectangle(25 + y,50 + y , 50 + y, 75 + y, fill =  "#" + format(color2, 'x') + "0000", width = "0" )
    color2 = color2 +7

for y in range(1,100, 15):
    w.create_rectangle(50 ,600 + y , 100 , 650 + y, fill =  "#" + format(color3, 'x') + "0000", width = "0" )
    color3 = color3 +10


w.pack()
root.mainloop()
