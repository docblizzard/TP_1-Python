from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="white", height=900, width=900)

w.create_oval(90 , 90, 800 ,800)

w.create_oval(80 , 400, 280 ,600)


w.create_oval(120 , 400, 400 ,700)


w.create_oval(190 , 360, 600 ,790)

w.create_oval(350, 210, 900 ,740)

w.create_oval(340, 80, 725 ,440)

w.create_oval(270, 230, 550 ,520)

w.create_oval(70, 70, 215 ,215)

w.create_oval(230, 210, 290 ,270)

w.create_oval(200, 340, 210 ,350)


w.pack()
root.mainloop()
