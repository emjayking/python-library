from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv

# ------------------------------- setup -------------------------------------- #
# ------------ Windows ----------- #
# This is the main gui window that all the gui is stored in
root = Tk()
root.title("Comic Book Store")

# ------------- Variables -------- #

chosen_option = StringVar() # What comic the user currently has selected
restock_amount = StringVar() # The amount the user wants to restock
status_str = StringVar() # An error readout for the user to see if they've done something wrong
comics_sold = IntVar() # How many comics the user has sold, is saved inbetween runs

comics_dict = {} # A dictionary of the comic class instances, indexed by their name (Comic name: Comic instance)

compiled_data = [["comic_name","stock"],] # Used for saving the data at the end of the session

status_str.set("startup succesfull!")

# -------- Frame Setup ----------- #
# Frames are like borders that group elements within windows.
# Used to help group the elements which makes the program easier to understand
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
    """This class is for a comic so that the user an add as many comics as they want into the gui without hard coding. instead they can just edit the data.txt file """

    def __init__(self, name, stock):
        self.stock = int(stock) # This is where each comic's stock is stored
        self.name = name

        # This sets the text that the user sees on screen
        self.text_variable = StringVar()
        self.text_variable.set("{} stock: {}".format(name, self.stock))

        # This creates the label the user sees on screen
        self.label = Label(stock_frame, textvariable=self.text_variable)
        self.label.pack(padx=10, pady=5)

    def _sell(self):
        """This Function sells one comic, the sell function further down simply figures out what comic the user has chosen and then calls that instance's sell function (this function)"""
        if self.stock > 0: # Check that the user cannot sell comics they do not own
            self.stock -= 1
            status_str.set("Succesfully sold")
            comics_sold.set(comics_sold.get() + 1)
            self.text_variable.set("{} stock: {}".format(self.name, self.stock))
        else:
            status_str.set(" Error. cannot sell stock you do not own!")


    def _restock(self):
        """This function acts the same as the sell function above, instead it takes the amount in the restock_amount variable from the restock_input element and adds that too the user's stock"""
        try:
            amount = int(restock_amount.get())
            self.stock += amount

            self.text_variable.set("{} stock: {}".format(self.name, self.stock))

            status_str.set("Succesfully Restocked")

        except:
            status_str.set("Error. do not use decimals or letters please")





# -------- Functions ------------ #
def sell():
    """Figures out what comic the user has chosen and then calls that comics sell function"""
    option = chosen_option.get()
    try:
        comics_dict[option]._sell()
    except:
        status_str.set("Please choose a comic!")


def restock():
    """Works the same way as the sell function"""
    option = chosen_option.get()
    try:
        comics_dict[option]._restock()
    except:
        status_str.set("Please choose a comic!")


#------------------- CSV Read-in ------------------------- #
# This segment reads the data.txt file and creates the comic classes as well as setting up the comics_sold variable.

with open('data.txt', mode='r+', newline='') as data:
    reader = csv.reader(data)
    row_num = 0
    # Loops through each line of the file
    for row in reader:
        # if it's the amount sold then update the onscreen var
        if row[0] == "_amount_sold":
            comics_sold.set(int(row[1]))

        # Otherwise assume it's a comic (exclude the first row)
        elif row_num != 0:
            class_name = row[0].strip()
            class_name = Comic(row[0], row[1]) # create the class instance
            comics_dict[row[0]] = class_name # Add it too the dictionary
            row_num +=1
        else:
            row_num +=1
    data.close()

# ------------------ GUI code main---------------------------- #

label1 = Label(sell_frame, text="Comic: ")
label1.grid(row=0, column=0, padx=10, pady=5)

#This allows the user to select what comic they want to sell/restock
comic_selector = ttk.OptionMenu(sell_frame, chosen_option, "choose a comic", * comics_dict.keys())
comic_selector.grid(row=0, column=1, padx=10, pady=5)

# ------ Sell -------- #
# The user clicks this button whenever they want to sell a comic
sell_button = Button(
sell_frame, text="Sell", command=sell, activebackground="blue", state="normal"
)
sell_button.grid(row=0, column=2, padx=10, pady=5)

# ------ Restock ----- #

restock_label = Label(restock_frame, text="Amount to restock: ")
restock_label.grid(row=0, column=0, padx=5, pady=5)

# The user clicks this to restock a chosen comic
restock_button = Button(restock_frame, text="Restock", command=restock, activebackground="blue", state="normal")
restock_button.grid(row=0, column=2, padx=10, pady=5)

# The user types in the amount they want to restock here
restock_input = Entry(restock_frame, textvariable=restock_amount)
restock_input.grid(row=0, column=1, padx=5, pady=5)


# ------- Status ----- #
# This shows what the outcome of the user's most recent action was, if it was a success or fail etc
status = Label(status_frame, textvariable=status_str)
status.grid(row=0, column=0, padx=10, pady=5)

# This shows the user what the total number of comics they've sold is
amount_sold_text = Label(status_frame, text="Number of comics sold:")
amount_sold_text.grid(row=1, column=0, padx=10, pady=5)

amount_sold = Label(status_frame, textvariable=comics_sold)
amount_sold.grid(row=1, column=1, padx=10, pady=5)

# ----- Stuff n Things ----- #
# Opens the gui window
root.mainloop()

# Update the data to write
for name, data in comics_dict.items():
    compiled_data.append([name, data.stock])

# Add the comics sold
compiled_data.append(["_amount_sold", comics_sold.get()])

# Update the data.txt file
with open('data.txt', mode='r+', newline='') as data:
    writer = csv.writer(data)
    writer.writerows(compiled_data)
    data.close()
