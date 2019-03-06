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

# ------------ Windows ----------- #
root = Tk()
root.title("Comic Book Store")

# ------------- Variables -------- #
restock_num = IntVar()
chosen_option = StringVar()
super_label_text = StringVar()
lizard_label_text = StringVar()
water_label_text = StringVar()
status_str = StringVar()
stocks = [8, 12, 3]
comics = ["Super Dude", "Lizard Man", "Water Woman"]

# --------- Variable setup ------- #
lizard_label_text.set("Lizard Man Stock: {}".format(stocks[1]))
water_label_text.set("Water Woman Stock: {}".format(stocks[2]))
super_label_text.set("Super Dude Stock: {}".format(stocks[0]))
status_str.set("Startup Succesfull")

# -------- Frame Setup ----------- #

status_frame = ttk.Frame(root)
status_frame.grid(row=2, column=0, sticky="NSEW", padx=10, pady=5)

sell_frame = ttk.Frame(root)
sell_frame.grid(row=0, column=0, sticky="NSEW", padx=10, pady=5)

stock_frame = ttk.Frame(root)
stock_frame.grid(row=1, column=0, sticky="NSEW", padx=10, pady=5)

# -------- Functions ------------ #
def sell():
    comic = chosen_option.get()
    if comic == "Super Dude":
        if stocks[0] > 0:
            stocks[0] -= 1
            super_label_text.set("Super Dude Stock: {}".format(stocks[0]))
            status_str.set("Sell attempt succesfull")
        else:
            status_str.set("Sell attempt failed, stock is at 0")
    elif comic == "Lizard Man":
        if stocks[1] > 0:
            stocks[1] -= 1
            lizard_label_text.set("Lizard Man Stock: {}".format(stocks[1]))
            status_str.set("Sell attempt succesfull")
        else:
            status_str.set("Sell attempt failed, stock is at 0")
    else:
        if stocks[2] > 0:
            stocks[2] -= 1
            water_label_text.set("Water Woman Stock: {}".format(stocks[2]))
            status_str.set("Sell attempt succesfull")
        else:
            status_str.set("Sell attempt failed, stock is at 0")

# ------------------ GUI code main---------------------------- #

super_dude_stock = Label(stock_frame, textvariable=super_label_text)
super_dude_stock.grid(row=1, column=0, padx=10, pady=5)

lizard_man_stock = Label(stock_frame, textvariable=lizard_label_text)
lizard_man_stock.grid(row=2, column=0, padx=10, pady=5)

water_woman_stock = Label(stock_frame, textvariable=water_label_text)
water_woman_stock.grid(row=3, column=0, padx=10, pady=5)

label1 = Label(sell_frame, text="Comic: ")
label1.grid(row=0, column=0, padx=10, pady=5)

comic_selector = ttk.OptionMenu(sell_frame, chosen_option, comics[0], * comics)
comic_selector.grid(row=0, column=1, padx=10, pady=5)

sell_button = Button(
sell_frame, text="Sell", command=sell, activebackground="blue", state="normal"
)
sell_button.grid(row=0, column=2, padx=10, pady=5)


status = Label(status_frame, textvariable=status_str)
status.grid(row=0, column=0, padx=10, pady=5)

# ----------------- Stuff n Things
root.mainloop()
