from tkinter import *
import random

root = Tk()
w = Canvas(root, bg="white", height=900, width=900)


w.create_rectangle(0, 0, 50, 50, fill = "#00ff00", outline = "red" )


w.pack()
root.mainloop()
