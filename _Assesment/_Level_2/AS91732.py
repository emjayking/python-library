# Author: Matthew King
# last edited: 12/02/19
# purpose : to get credits
# verion num: 1.0
# notes: this is version 1.0 because it is the first working version that is fully complete any major changes will increase it to 1.1 and any minor changes will make it 1.01 etc. 
print('hello world')
# ---------------------------------- Variables ------------------------------- #
items = {} # dictionary that stores all the information
average_price = 0 # the average price of all the products
cheapest_item = ["", 0] # the cheapest item listed
dearest_item = ["", 0] # the most expensive item listed
remaining_budget = 0 # this will be used to calculate how many items the user can buy
cheapest_unit_cost = ["", 0]
recomendation = [] # what the user should buy
units_of_measurement = ["kg", "g", "ml", "l"]
# ---------------------------------- Functions ------------------------------- #
def enter_value(name):
    # basic info for each product
    item = {
    "price": 00.00,
    "unit": "",
    "mass": 0,
    }
    for value in item: # loop to create a dictionary for the product
        # basic 'if' logic to help with grammar
        while True:
            try:
                if value == "unit":
                    item[value] = str(input("please choose between kg, g, ml or l to use as the unit of measurement for this product  ").strip())
                    if item[value] in units_of_measurement:
                        print("that is not an acceptable unit, please try again")
                        continue


                elif value == "mass": #
                    item[value] = int(input("how many {}s are in the product?".format(item["unit"])))

                elif value == "price":
                    item[value] = float(input("what is the price of the product?  $:"))
                    if item[value] > 200:
                        print("That's too expensive! try again")
                        continue
                    elif item[value] < 0.10:
                        print("that's too cheap, try again")
                        continue

                break
            except ValueError:
                print("Error, try again")

    product_values = item
    return product_values


def find_cheapest():
    for name, value in items.items():
        if values["unit_cost"] < cheapest_unit_cost[1]:
            cheapest_unit_cost = [name, values["unit_cost"]]

# ------------------------------- Code ------------------------------ #
while True:
    while True:
        try:
            budget = float(input("what is your budget?   $:"))
            #-------- Add conditions for reasonable boundaries -------#
            if budget > 300.0:
                print("I think that's a bit unlikely, please enter a more reasonable amount")
                continue
            elif budget <= 0:
                print("this isn't a charity, you can't buy anything with that amount")
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
        confirm = input("do you want to enter another product? y/n   :")
        if confirm == "n":
            break

    # print(items)
    # When the user exits the loop, display summary values
    for name, values in items.items():
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
    for name, values in items.items():
        # convert all units to kg
        if values["unit"] == "g" or values["unit"] == "ml":
            values["mass"] /= 1000
        # for the sake of my sanity, 1 litre = 1 kilogram

        # calculate 'value' as 'unit cost'
        values["unit_cost"] = values["price"] / values["mass"]

        #find the lowest 'unit_cost'
        if values["unit_cost"] < cheapest_unit_cost[1]:
            cheapest_unit_cost = [name, values["unit_cost"]]
    # recomend the best value for money that fits the user's budget
    remaining_budget = budget
    for name, values in items.items():
        if values["unit_cost"] == [cheapest_unit_cost[1]] and values["price"] < remaining_budget:
            recomendation.append(name)
            remaining_budget -= values["price"]
            del items["name"]
            find_cheapest()
    if recomendation != []:
        print("I would recomend you buy:" + recomendation)
    else:
        print("You can't buy any of the products you entered with the budget you have")

# Give user option to restart or exit.
    restart = input("would you like to restart?   y/n:  ")
    if restart == "n":
        break
