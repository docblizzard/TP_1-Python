from tkinter import *

root = Tk()
w = Canvas(root, bg="lightgray", height=300, width=300)

for j in range(10, 135, 15):
    c0 = w.create_oval(0 + j, 300-j, 300 - j, 0 + j)

w.pack()
root.mainloop()
