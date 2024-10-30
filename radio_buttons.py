from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Working with Frames")

r = IntVar()
r.set("2")


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

my_label = Label(root, text=r.get())
my_label.pack()

my_button = Button(root, text="Click Me!", command=lambda: clicked(r.get())).pack()

root.mainloop()
