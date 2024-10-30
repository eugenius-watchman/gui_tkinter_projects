from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Working with MessageBox")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
