from tkinter import  *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Tkinter Graphs")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 500)
    plt.show()

my_button = Button(root, text="Show Graph(s)", command=graph)
my_button.pack()

root.mainloop()