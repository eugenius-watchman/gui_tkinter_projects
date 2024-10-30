from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Working with Windows Viewer Sliders")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=400, orient="horizontal")
horizontal.pack()

my_label = Label(root, text=horizontal.get())
my_label.pack()

my_btn = Button(root, text="Click Me!", command=slide)
my_btn.pack()

root.mainloop()
