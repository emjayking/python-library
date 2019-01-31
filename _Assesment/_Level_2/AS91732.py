# 31/01/19, basic plan and starter code
# TO DO: add boundary conditions. baby proof code, plan this $%!#, allow the user to choose their units. rework function
# Ask user how much cash they have, (must be reasonable amount i.e. $10)
print('hello world')
# ---------------------------------- Variables ------------------------------- #
items = {} # dictionary that stores all the information
average_price = 0 # the average price of all the products
cheapest_item = ["", 0] # the cheapest item listed
dearest_item = ["", 0] # the most expensive item listed
remaining_budget = 0 # this will be used to calculate how many items the user can buy
# ---------------------------------- Functions ------------------------------- #
def enter_value(name):
    # basic info for each product
    item = {
    "price": "",
    "unit": "",
    "mass": "",
    }
    for value in item: # loop to create a dictionary for the product
        # basic 'if' logic to help with grammar
        if value == "unit":
            item[value] = input("please choose between kg, g, ml or l to use as the unit of measurement for this product  ")

        elif value == "mass": #
            item[value] = input("how many {} are in the product?".format(item["unit"]))

        # standard question for all other infor
        item[value] = input("what is the {} of the product?  ".format(value))

    product_values = item
    return product_values

# ------------------------------- Code ------------------------------ #

while True:
    try:
        cash = float(input("what is your budget?   $:"))
        #-------- Add conditions for reasonable boundaries -------#
        break
    except ValueError:
        print("Error, try again")
# Loop

for i in range(100): # can't imagine any students using a budget calculator buying more than 100 packs of instant noodles

    # Enter product info (name weight/volume, price etc)
    product_name = input("what is the name of the product?")
    items[product_name] = enter_value(product_name)

    # Ask to continue
    confirm = "n"
    confirm = input("do you want to continue y/n   :")
    if confirm == "n":
        break

print(items)
# When the user exits the loop, display summary values
for name, values in items.items()
    # Item name and unit price for each item in the list
    print("{} costs ${}".format(name, values["price"]))
    # Avg price
    average_price += values["price"]
    # Cheapest Item
    if values["price"] < cheapest_item[1]:
        cheapest_item = [name, values["price"]]
    # Most Expensive Item
    if values["price"] > dearest_item[1]:
        dearest_item = [name, values["price"]]

# ---------------------------------- purchase logic ------------------------- #

# calculate the 'value' of the product as a function of cost//mass(kg)

    # convert all units to kg

    # calculate 'value' as 'unit cost'

# recomend the best value for money that fits the user's budget

# Give user option to restart or exit.
