from tkinter import  *
from PIL import ImageTk, Image
from tkinter import messagebox

# from image3 import my_label
# from sliders import horizontal, my_btn

root = Tk()
root.title("Working with Windows Viewer Sliders")
root.geometry("400x400")

# create vertical scale
vertical = Scale(root, from_=0, to=200)
vertical.pack()

# create horizontal scale
horizontal = Scale(root, from_=0, to=400, orient="horizontal")
horizontal.pack()

# create label to display horizontal scale value
my_label = Label(root, text=horizontal.get())
my_label.pack()

# function to update window size and label text
def slide():
    # update label text
    my_label.config(text=horizontal.get())
    #resize the window on the slider values
    root.geometry(f"{horizontal.get()}x{vertical.get()}")

# button to trigger the slide function
my_btn = Button(root, text="Click Me!", command=slide)
my_btn.pack()

root.mainloop()