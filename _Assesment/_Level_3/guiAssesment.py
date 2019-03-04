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

restock_window = Tk()
restock_window.title("Restock Window")

restock_num = IntVar()
stocks = [8, 12, 3]

# ------------------------------ GUI code ------------------------------------ #
super_dude_stock = Label(root, textvariable=restock_num)
super_dude_stock.pack()

lizard_man_stock = Label(root, text="error 404 content not found")
lizard_man_stock.pack()

water_woman_stock = Label(root, text="BETA feature, testing in progress")

restock_entry = Entry(restock_window, textvariable=restock_num)
restock_entry.pack()



root.mainloop()
