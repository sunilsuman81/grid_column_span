from tkinter import *

window = Tk()
r = Label(bg="red", width=20, height=10)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=10)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=10)
b.grid(row=2, column=0, columnspan=2)



window.mainloop()
