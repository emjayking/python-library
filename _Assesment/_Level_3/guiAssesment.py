from tkinter import *
from tkinter import ttk
import tkinter as tk

# ------------------------------- setup -------------------------------------- #
# ------------ Windows ----------- #
root = Tk()
root.title("Comic Book Store")

# ------------- Variables -------- #
chosen_option = StringVar()
super_label_text = StringVar()
lizard_label_text = StringVar()
water_label_text = StringVar()
restock_amount = StringVar()
status_str = StringVar()
comics_sold = IntVar()
stocks = [8, 12, 3]
comics = ["Super Dude", "Lizard Man", "Water Woman"]

# --------- Variable setup ------- #
lizard_label_text.set("Lizard Man Stock: {}".format(stocks[1]))
water_label_text.set("Water Woman Stock: {}".format(stocks[2]))
super_label_text.set("Super Dude Stock: {}".format(stocks[0]))
status_str.set("Startup Succesfull")

# -------- Frame Setup ----------- #
sell_frame = ttk.Frame(root)
sell_frame.grid(row=0, column=0, sticky="NS", padx=10, pady=5)

stock_frame = ttk.Frame(root)
stock_frame.grid(row=1, column=0, sticky="NS", padx=10, pady=5)

restock_frame = ttk.Frame(root)
restock_frame.grid(row=3, column=0, sticky="NSEW", padx=10, pady=5)

status_frame = ttk.Frame(root)
status_frame.grid(row=4, column=0, sticky="NS", padx=10, pady=5)



# -------- Functions ------------ #
def sell():
    comic = chosen_option.get()
    if comic == "Super Dude":
        if stocks[0] > 0:
            stocks[0] -= 1
            super_label_text.set("Super Dude Stock: {}".format(stocks[0]))
            status_str.set("Sell attempt succesfull")
            comics_sold.set(int(comics_sold.get()) + 1)
        else:
            status_str.set("Sell attempt failed, stock is at 0")
    elif comic == "Lizard Man":
        if stocks[1] > 0:
            stocks[1] -= 1
            lizard_label_text.set("Lizard Man Stock: {}".format(stocks[1]))
            status_str.set("Sell attempt succesfull")
            comics_sold.set(int(comics_sold.get()) + 1)
        else:
            status_str.set("Sell attempt failed, stock is at 0")
    else:
        if stocks[2] > 0:
            stocks[2] -= 1
            water_label_text.set("Water Woman Stock: {}".format(stocks[2]))
            status_str.set("Sell attempt succesfull")
            comics_sold.set(int(comics_sold.get()) + 1)
        else:
            status_str.set("Sell attempt failed, stock is at 0")

def restock():
    # Make sure the user doesn't enter any decimals or words
    try:
        amount = int(restock_amount.get())
    except:
        status_str.set("Error, whole numbers only please!")

    comic = chosen_option.get()
    if comic == "Super Dude":
        stocks[0] += amount
        super_label_text.set("Super Dude Stock: {}".format(stocks[0]))
        status_str.set("Restock attempt succesfull")
    elif comic == "Lizard Man":
        stocks[1] += amount
        lizard_label_text.set("Lizard Man Stock: {}".format(stocks[1]))
        status_str.set("Restock attempt succesfull")
    else:
        stocks[2] += amount
        water_label_text.set("Water Woman Stock: {}".format(stocks[2]))
        status_str.set("Restock attempt succesfull")

# ------------------ GUI code main---------------------------- #

label1 = Label(sell_frame, text="Comic: ")
label1.grid(row=0, column=0, padx=10, pady=5)

comic_selector = ttk.OptionMenu(sell_frame, chosen_option, comics[0], * comics)
comic_selector.grid(row=0, column=1, padx=10, pady=5)

# ------ Stocks ------ #

super_dude_stock = Label(stock_frame, textvariable=super_label_text)
super_dude_stock.grid(row=1, column=0, padx=10, pady=5)

lizard_man_stock = Label(stock_frame, textvariable=lizard_label_text)
lizard_man_stock.grid(row=2, column=0, padx=10, pady=5)

water_woman_stock = Label(stock_frame, textvariable=water_label_text)
water_woman_stock.grid(row=3, column=0, padx=10, pady=5)

# ------ Sell -------- #

sell_button = Button(
sell_frame, text="Sell", command=sell, activebackground="blue", state="normal"
)
sell_button.grid(row=0, column=2, padx=10, pady=5)

# ------ Restock ----- #

restock_label = Label(restock_frame, text="Amount to restock: ")
restock_label.grid(row=0, column=0, padx=5, pady=5)

restock_button = Button(restock_frame, text="Restock", command=restock, activebackground="blue", state="normal")
restock_button.grid(row=0, column=2, padx=10, pady=5)

restock_input = Entry(restock_frame, textvariable=restock_amount)
restock_input.grid(row=0, column=1, padx=5, pady=5)


# ------- Status ----- #

status = Label(status_frame, textvariable=status_str)
status.grid(row=0, column=0, padx=10, pady=5)

amount_sold_text = Label(status_frame, text="Number of comics sold:")
amount_sold_text.grid(row=1, column=0, padx=10, pady=5)

amount_sold = Label(status_frame, textvariable=comics_sold)
amount_sold.grid(row=1, column=1, padx=10, pady=5)

# ----- Stuff n Things ----- #
root.mainloop()
