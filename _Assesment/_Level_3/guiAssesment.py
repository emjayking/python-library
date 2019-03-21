from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv

# ------------------------------- setup -------------------------------------- #
# ------------ Windows ----------- #
root = Tk()
root.title("Comic Book Store")

# ------------- Variables -------- #
chosen_option = StringVar()
restock_amount = StringVar()
status_str = StringVar()
comics_sold = IntVar()
comics_dict = {'comic_name': 'stock',}
name = ""

status_str.set("startup succesfull!")

# -------- Frame Setup ----------- #
sell_frame = ttk.Frame(root)
sell_frame.grid(row=0, column=0, sticky="NS", padx=10, pady=5)

stock_frame = ttk.Frame(root)
stock_frame.grid(row=1, column=0, sticky="NS", padx=10, pady=5)

restock_frame = ttk.Frame(root)
restock_frame.grid(row=3, column=0, sticky="NSEW", padx=10, pady=5)

status_frame = ttk.Frame(root)
status_frame.grid(row=4, column=0, sticky="NS", padx=10, pady=5)
# -------- Class setup ---------- #

class Comic:
    """This class is for a comic so it auto generates all the labels and stuff cause I'm lazy """

    def __init__(self, name, stock):
        self.stock = int(stock)
        self.name = name

        self.text_variable = StringVar()
        self.text_variable.set("{} stock: {}".format(name, self.stock))

        self.label = Label(stock_frame, textvariable=self.text_variable)
        self.label.pack(padx=10, pady=5)


    def _sell(self):
        if self.stock > 0:
            self.stock -= 1
            status_str.set("Succesfully sold")
            comics_sold.set(comics_sold.get() + 1)
            self.text_variable.set("{} stock: {}".format(self.name, self.stock))
        else:
            status_str.set(" Error. cannot sell stock you do not own!")


    def _restock(self):
        try:
            amount = int(restock_amount.get())
            self.stock += amount

            self.text_variable.set("{} stock: {}".format(self.name, self.stock))

            status_str.set("Succesfully Restocked")

        except:
            status_str.set("Error. do not use decimals or letters please")





# -------- Functions ------------ #
def sell():
    option = chosen_option.get()
    try:
        comics_dict[option]._sell()
    except:
        status_str.set("Please choose a comic!")


def restock():
    option = chosen_option.get()
    try:
        comics_dict[option]._restock()
    except:
        status_str.set("Please choose a comic!")


#------------------- CSV Read-in ------------------------- #
with open('data.txt', mode='r') as data:
    reader = csv.reader(data)
    print(reader)
    row_num = 0
    for row in reader:
        if row[0] == "_amount_sold":
            comics_sold.set(int(row[1]))
        elif row_num != 0:
            class_name = row[0].strip()
            class_name = Comic(row[0], row[1])
            comics_dict[row[0]] = class_name
            row_num +=1
        else:
            row_num +=1
    data.close()

# ------------------ GUI code main---------------------------- #

label1 = Label(sell_frame, text="Comic: ")
label1.grid(row=0, column=0, padx=10, pady=5)

comic_selector = ttk.OptionMenu(sell_frame, chosen_option, "choose a comic", * comics_dict.keys())
comic_selector.grid(row=0, column=1, padx=10, pady=5)

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

with open('data.txt', mode='rw') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    reader = csv.reader(data)

    row_num = 0

    data.close()
