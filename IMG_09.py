from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="white", height=900, width=900)

w.create_oval(95 , 95, 750 ,750, width = "1")

w.create_oval(120, 120 , 600 ,600, width = "1")

w.create_oval(140, 140 , 500 ,500,width = "1")

w.create_oval(155, 155 , 420 ,420, width = "1")

w.create_oval(170, 170 , 350 ,350, width = "1")

w.create_oval(175, 175 , 310 ,310, width = "1")

w.create_oval(180, 180 , 280 ,280, width = "1")

w.create_oval(187, 187 , 250 ,250, width = "1")

w.create_oval(190, 190 , 235 ,235, width = "1")

w.create_oval(192, 192 , 225 ,225, width = "1")

w.create_oval(194, 194 , 215 ,215, width = "1")

w.pack()
root.mainloop()
