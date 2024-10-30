from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# load images
my_img = ImageTk.PhotoImage(Image.open("images/art2.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/art3.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/art4.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/art5.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/art6.jpg"))

image_list = [my_img, my_img2, my_img3, my_img4, my_img5]

# display first image
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


# functionalities to handle buttons
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    # put onscreen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # put onscreen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# definitions
button_back = Button(root, text="<<", command=lambda: back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# on screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
