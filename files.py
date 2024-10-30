from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Working with Files")
img = PhotoImage("/home/eugene/PycharmProjects/GUI_Tkinter/favicon.ico")
root.tk.call('wm', 'iconphoto', root._w, img)


def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/home/eugene/GUI_Tkinter/images", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename)
    my_label.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open_file)
my_btn.pack()

root.mainloop()
