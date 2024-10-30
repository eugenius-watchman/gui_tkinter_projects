from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# Set fixed window size (e.g., 400x400 pixels)
root.geometry("400x450")
root.resizable(False, False)

# Load and resize images to fit the fixed window size
def load_and_resize_image(path, size=(400, 400)):
    img = Image.open(path)

    # Check for LANCZOS
    if hasattr(Image, "LANCZOS"):
        img = img.resize(size, Image.LANCZOS)
    else:
        img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load images
my_img = load_and_resize_image("images/art2.jpeg")
my_img2 = load_and_resize_image("images/art3.jpg")
my_img3 = load_and_resize_image("images/art4.jpg")
my_img4 = load_and_resize_image("images/art5.jpg")
my_img5 = load_and_resize_image("images/art6.jpg")

image_list = [my_img, my_img2, my_img3, my_img4, my_img5]

# Display first image
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

# Button functionalities
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    # Update buttons
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable forward button on the last image
    if image_number == len(image_list):
        button_forward.config(state=DISABLED)
        button_forward = Button(root, text=">>", state=DISABLED)

    # Display image and buttons
    # my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    # Update buttons
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Disable back button on the first image
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Display image and buttons
    # my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Define buttons
button_back = Button(root, text="<<", command=lambda: back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Display buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
