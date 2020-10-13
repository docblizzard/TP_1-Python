from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="black", height=900, width=900)

w.create_rectangle(0, 0, 180, 180, fill="red", outline="red")

w.create_rectangle(720, 0, 900, 180, fill="red", outline="red")

w.create_rectangle(0, 720, 180, 900, fill="red", outline="red")

w.create_rectangle(720, 720, 900, 900, fill="red", outline="red")

w.create_rectangle(360, 0, 540, 540, fill="red", outline="red")

w.create_rectangle(0, 360, 540, 540, fill="red", outline="red")

w.create_rectangle(360, 540, 540, 900, fill="white", outline="white")

w.create_rectangle(540, 360, 900, 540, fill="white", outline="white")
w.pack()
root.mainloop()
