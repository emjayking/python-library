# 31/01/19, basic plan and starter code
# TO DO: add boundary conditions. baby proof code, plan this $%!#, allow the user to choose their units. rework function
# Ask user how much cash they have, (must be reasonable amount i.e. $10)
print('hello world')

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
items = {}
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

    # Item name and unit price for each item in the list

    # Avg price

    # Cheapest Item

    # Most Expensive Item

# Recomend what item/s to purchase based on

    # permutate the items until a combination that maximises volume while   fitting budget is found.

# Give user option to restart or exit.
