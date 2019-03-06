'''
The comic book stores the following comics:

Super Dude - Starting with 8 in stock
Lizard Man - Starting with 12 in stock
Water Woman - Starting with 3 in stock

The user should be able to sell a comic one at a time, reducing the stock by one.

The interface should notify the user if the comic has been sold successfully.
The interface should notify the user with an error message if the comic has not been sold if there is
not enough stock.

The interface should display:
The number of comics sold.
The current stock levels of all comics (at once). If the stock levels change at any point, the
interface should update.

The user should be able to restock a chosen comic.
The user should be able to input how many copies the comic is being restocked with. For example, restock 10 copies of Super Dude at once.

There is no limit to the amount of comics the store can stock.
The program should display relevant error messages for appropriate situations.
'''
from tkinter import *
from tkinter import ttk
import tkinter as tk

# ------------------------------- setup -------------------------------------- #
root = Tk()
root.title("Comic Book Store")

restock_num = IntVar()
stocks = [8, 12, 3]

chosen_option = StringVar()

comics = ["Super Dude", "Lizard Man", "Water Woman"]

def sell():
    comic = chosen_option.get()
    if comic == "Super Dude":
        stocks[0] -= 1
    elif comic == "Lizard Man":
        stocks[1] -= 1
    else:
        stocks[2] -= 1

# ------------------ GUI code main---------------------------- #

super_dude_stock = Label(root, textvariable=)
super_dude_stock.grid(row=1, column=0, padx=10, pady=5)

lizard_man_stock = Label(root, textvariable=stocks[1])
lizard_man_stock.grid(row=2, column=0, padx=10, pady=5)

water_woman_stock = Label(root, textvariable=stocks[2])
water_woman_stock.grid(row=3, column=0, padx=10, pady=5)

label1 = Label(root, text="Comic: ")
label1.grid(row=0, column=0, padx=10, pady=5)

comic_selector = ttk.OptionMenu(root, chosen_option, comics[0], * comics)
comic_selector.grid(row=0, column=1, padx=10, pady=5)

sell_button = Button(
root, text="Sell", command=sell, activebackground="blue", state="normal"
)

sell_button.grid(row=0, column=2, padx=10, pady=5)



# ----------------- Stuff n Things
root.mainloop()
