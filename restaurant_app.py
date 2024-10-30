import tkinter as tk
from tkinter import Label, Button
import time

# time for user when working
localtime = time.asctime(time.localtime(time.time()))


class App1:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        # fonts

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 20 bold"
        font12 = "Al-aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        # __variables for calculations__
        self.waakye_rice_var = tk.DoubleVar()
        self.garri_macaroni_var = tk.DoubleVar()
        self.fried_plantain_var = tk.DoubleVar()
        self.meat_fish_hide_var = tk.DoubleVar()
        self.boiled_egg_var = tk.DoubleVar()
        self.veg_salad_var = tk.DoubleVar()
        self.drinks_var = tk.DoubleVar()

        self.cost_var = tk.StringVar()
        self.service_charge_var = tk.StringVar()
        self.tax_var = tk.StringVar()
        self.subtotal_var = tk.StringVar()
        self.total_var = tk.StringVar()

        # ___food info___

        self.Label1 = tk.Label(master=top, text='WAAKYE PALAVA SYSTEM', background="#091833", font=font11,
                               foreground="#f2a343")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)

        localtime1 = tk.Label(master=top, text=localtime, background="#091833", font=font16, fg="steel blue")
        localtime1.place(relx=0.420, rely=0.12)


        # ___label food___

        self.label12 = tk.Label(master=top, text='Order Num. :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.25)

        self.label12 = tk.Label(master=top, text='Waakye/Rice :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.32)

        self.label12 = tk.Label(master=top, text='Garri/Macaroni :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.4)

        self.label12 = tk.Label(master=top, text='Fried Plantain :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.48)

        self.label12 = tk.Label(master=top, text='Meat/Fish/Hide :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.56)

        self.label12 = tk.Label(master=top, text='Boiled Egg :', foreground="#bac8bd", font=font12,
                                background="#091833")
        self.label12.place(relx=0.054, rely=0.64)

        self.label12 = tk.Label(master=top, text='Veg Salad :', foreground="#bac8bd", font=font12, background="#091833")
        self.label12.place(relx=0.054, rely=0.71)

        self.label12 = tk.Label(master=top, text='Drinks :', foreground="#ff00ff", font=font12, background="#091833")
        self.label12.place(relx=0.054, rely=0.77)


        # __ entry for food__

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.20, rely=0.24)

        self.waakye_rice_entry = tk.Entry(master=top, background="#d9d9d9",  textvariable=self.waakye_rice_var, foreground="#c60000", selectbackground="#f2a343",
                                    font=font13)
        self.waakye_rice_entry.place(relx=0.20, rely=0.31)

        self.garri_macaroni_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.garri_macaroni_var,  foreground="#c60000",
                                       selectbackground="#f2a343", font=font13)
        self.garri_macaroni_entry.place(relx=0.20, rely=0.39)

        self.fried_plantain_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.fried_plantain_var, foreground="#c60000",
                                       selectbackground="#f2a343", font=font13)
        self.fried_plantain_entry.place(relx=0.20, rely=0.47)

        self.meat_fish_hide_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.meat_fish_hide_var, foreground="#c60000",
                                       selectbackground="#f2a343", font=font13)
        self.meat_fish_hide_entry.place(relx=0.20, rely=0.55)

        self.boiled_egg_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.boiled_egg_var, foreground="#c60000", selectbackground="#f2a343",
                                   font=font13)
        self.boiled_egg_entry.place(relx=0.20, rely=0.63)

        self.veg_salad_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.veg_salad_var, foreground="#c60000", selectbackground="#f2a343",
                                  font=font13)
        self.veg_salad_entry.place(relx=0.20, rely=0.70)

        self.drinks_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.drinks_var, foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.drinks_entry.place(relx=0.20, rely=0.77)

        # __ Calc __

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                               font=font13)
        self.entry1.place(relx=0.705, rely=0.24, height=35, relwidth=0.267)

        self.Button1 = tk.Button(master=top, text='''7''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''8''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''9''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''/''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''4''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''5''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''6''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''*''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''1''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''2''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''3''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''-''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''0''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.64, height=44, width=146)
        self.Button1 = tk.Button(master=top, text='''.''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.64, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''+''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.64, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''=''', background="#f2a343", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.74, height=44, width=221)
        self.Button1 = tk.Button(master=top, text='''C''', background="#122c63", font=font14, foreground="#ffffff",
                                 borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.74, height=44, width=37)

        # __ cost __

        self.label12 = tk.Label(master=top, text='Cost :', foreground="#e16740", font=font12, background="#091833")
        self.label12.place(relx=0.40, rely=0.32)

        self.label12 = tk.Label(master=top, text='Service charge :', foreground="#bac8bd", font=font12, background="#091833")
        self.label12.place(relx=0.37, rely=0.4)

        self.label12 = tk.Label(master=top, text='Tax :', foreground="#bac8bd", font=font12, background="#091833")
        self.label12.place(relx=0.40, rely=0.48)

        self.label12 = tk.Label(master=top, text='Subtotal :', foreground="#bac8bd", font=font12, background="#091833")
        self.label12.place(relx=0.38, rely=0.56)

        self.label12 = tk.Label(master=top, text='Total :', foreground="#bac8bd", font=font12, background="#091833")
        self.label12.place(relx=0.40, rely=0.64)

        # __cost entry__

        self.cost_entry = tk.Entry(master=top, textvariable=self.cost_var, background="#d9d9d9", foreground="#c60000", selectbackground="#f2a343",
                             font=font13)
        self.cost_entry.place(relx=0.467, rely=0.31)

        self.service_charge_entry = tk.Entry(master=top, textvariable=self.service_charge_var, background="#d9d9d9", foreground="#c60000",
                                       selectbackground="#f2a343", font=font13)
        self.service_charge_entry.place(relx=0.516, rely=0.39, relwidth=0.111)

        self.tax_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.tax_var, foreground="#c60000", selectbackground="#f2a343",
                            font=font13)
        self.tax_entry.place(relx=0.467, rely=0.47)

        self.subtotal_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.subtotal_var, foreground="#c60000", selectbackground="#f2a343",
                                 font=font13)
        self.subtotal_entry.place(relx=0.479, rely=0.55, relwidth=0.149)

        self.total_entry = tk.Entry(master=top, background="#d9d9d9", textvariable=self.total_var, foreground="#c60000", selectbackground="#f2a343",
                              font=font13)
        self.total_entry.place(relx=0.466, rely=0.63)

        # __control buttons__

        self.Button2 = tk.Button(master=top, text='PRICE', background="#e16740", font=font16, command=self.calculate_price)
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='TOTAL', background="#e16740", font=font16, command=self.calculate_total)
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='RESET', background="#e16740", font=font16, command=self.reset)
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text='EXIT', background="#e16740", font=font16, command=top.quit)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)

    def calculate_price(self):
        # calculations for each food item
        try:
            cost_of_waakye_rice = self.waakye_rice_var.get() * 5  # assuming price per unit is 5
            cost_of_garri = self.garri_macaroni_var.get() * 2
            cost_of_plantain = self.fried_plantain_var.get() * 3
            cost_of_meat = self.meat_fish_hide_var.get() * 10
            cost_of_egg = self.boiled_egg_var.get() * 3
            cost_of_veg = self.veg_salad_var.get() * 5
            cost_of_drinks = self.drinks_var.get() * 5

            total_cost = (cost_of_waakye_rice + cost_of_garri + cost_of_plantain + cost_of_meat + cost_of_egg + cost_of_veg + cost_of_drinks)

            # update cost_var
            self.cost_var.set(f"₵{total_cost:.2f}")
        except Exception as e:
            self.cost_var.set("Error")

    def calculate_total(self):
        try:
            # Removing '₵' symbol and any spaces and converting to float
            cost = float(self.cost_var.get().replace('₵', '').strip())

            service_charge = cost * 0.1  # 10% service charge
            tax = cost * 0.05  # 5% tax
            subtotal = cost + service_charge + tax

            # Update variables
            self.service_charge_var.set(f"₵{service_charge:.2f}")
            self.tax_var.set(f"₵{tax:.2f}")
            self.subtotal_var.set(f"₵{subtotal:.2f}")
            self.total_var.set(f"₵{subtotal:.2f}")
        except ValueError:
            self.total_var.set("Error")

    def reset(self):
        self.waakye_rice_var.set(0)
        self.garri_macaroni_var.set(0)
        self.fried_plantain_var.set(0)
        self.meat_fish_hide_var.set(0)
        self.boiled_egg_var.set(0)
        self.veg_salad_var.set(0)
        self.drinks_var.set(0)
        self.cost_var.set("")
        self.service_charge_var.set("")
        self.tax_var.set("")
        self.subtotal_var.set("")
        self.total_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = App1(root)
    root.mainloop()
