from tkinter import *
from PIL import ImageTk, Image

from image3 import my_label

root = Tk()
root.title("Check Boxes")
root.geometry("400x400")

def show():
    # see what goes on behind the scene
    my_label = Label(root, text=var.get()).pack()



var = IntVar()
c = Checkbutton(root, text="Check box", variable=var)
c.pack()


my_button = Button(root, text="Show selection", command=show)
my_button.pack()


root.mainloop()