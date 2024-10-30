from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Working with MessageBox")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    messagebox.showinfo("This is my Popup!", "Hello World")
    messagebox.showwarning("This is my Popup!", "Hello World")
    messagebox.showerror("This is my Popup!", "Hello World")
    messagebox.askquestion("This is my Popup!", "Hello World")
    messagebox.askokcancel("This is my Popup!", "Hello World")
    messagebox.askyesno("This is my Popup!", "Hello World")


Button(root, text="Popup", command=popup).pack()

root.mainloop()
