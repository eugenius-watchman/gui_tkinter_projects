from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Working with Windows")
img = PhotoImage("/home/eugene/PycharmProjects/GUI_Tkinter/favicon.ico")
root.tk.call('wm', 'iconphoto', root._w, img)


def open_window():
    global my_img
    top = Toplevel()
    top.title("My Second Window")
    img = PhotoImage("/home/eugene/PycharmProjects/GUI_Tkinter/favicon.ico")
    root.tk.call('wm', 'iconphoto', root._w, img)
    my_img = ImageTk.PhotoImage(Image.open("images/art6.jpg"))
    my_label = (Label(top, image=my_img))
    my_label.pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open_window).pack()

root.mainloop()
