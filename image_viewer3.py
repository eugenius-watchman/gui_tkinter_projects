from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# Set fixed window size
root.geometry("400x500")
root.resizable(False, False)

# Load and resize images to fit the fixed window size
def load_and_resize_image(path, size=(400, 400)):
    img = Image.open(path)
    if hasattr(Image, 'LANCZOS'):
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

# Display the first image
my_label = Label(root, image=my_img)
my_label.grid(row=0, column=0, columnspan=3, pady=10)

# Button functionalities
def forward(image_number):
    global my_label

    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Update button states
    button_forward.config(command=lambda: forward(image_number + 1))
    button_back.config(command=lambda: back(image_number - 1))

    # Disable the forward button on the last image
    if image_number == len(image_list):
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)

    # Enable the back button
    button_back.config(state=NORMAL)

def back(image_number):
    global my_label

    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Update button states
    button_forward.config(command=lambda: forward(image_number + 1))
    button_back.config(command=lambda: back(image_number - 1))

    # Disable the back button on the first image
    if image_number == 1:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)

    # Enable the forward button
    button_forward.config(state=NORMAL)

# Initial button definitions and placement
button_back = Button(root, text="<<", command=lambda: back(1), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Place buttons on the grid with correct row and column, with padding to ensure visibility
button_back.grid(row=1, column=0, padx=10, pady=10)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
