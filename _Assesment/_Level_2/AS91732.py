# Author: Matthew King
# last edited: 20/02/19
# purpose : to get credits
# verion num: 2.0
# notes: this is version 1.x because it is the first working version that is fully complete any major changes will increase it to 1.x + 1 and any minor changes will make it 1.x + 0.1 etc.
print('hello world')
# ---------------------------------- Variables ------------------------------- #
items = {} # dictionary that stores all the information
average_price = 0 # the average price of all the products
cheapest_item = ["", 0] # the cheapest item listed
dearest_item = ["", 0] # the most expensive item listeds
remaining_budget = 0 # this will be used to calculate how many items the user can buy
recomendation = [] # what the user should buy
units_of_measurement = ["kg", "g", "ml", "l"]
item_list = []
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
                    item[value] = str(input("please choose between kg, g, ml or l to use as the unit of measurement for this product      ").strip())
                    if item[value] not in units_of_measurement:
                        print("that is not an acceptable unit, please try again")
                        continue


                elif value == "mass": #
                    item[value] = float(input("how many {}s are in the product?  ".format(item["unit"])))

                elif value == "price":
                    item[value] = float(input("what is the price of the product?  $: "))
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

# this will allow me to sort this list to find the cheapest unit cost

# ------------------------------- Code ------------------------------ #
while True:
    while True:
        try:
            budget = float(input("what is your budget?   $:"))
            if budget > 300.0:
                print("I think that's a bit unlikely, please enter a more reasonable amount")
                continue
            elif budget <= 0:
                print("this isn't a charity, you can't buy anything with that amount")
            break
        except ValueError:
            print("Error, try again")

    for i in range(100): # can't imagine any students using a budget calculator buying more than 100 packs of instant noodles

        # Enter product info (name weight/volume, price etc)
        product_name = input("what is the name of the product?")
        items[product_name] = enter_value(product_name)

        # Ask to continue
        confirm = "n"
        confirm = input("do you want to enter another product? y/n   :")
        if confirm == "n":
            break

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

    # ---------------------------------- purchase logic ---------------------- #

    # calculate the 'value' of the product as a function of cost//mass(kg)
    for name, values in items.items():
        # convert all units to kg
        if values["unit"] == "g" or values["unit"] == "ml":
            values["mass"] /= 1000
        # for the sake of my sanity, 1 litre = 1 kilogram
        # calculate 'value' as 'unit cost'
        values["unit_cost"] = float(values["price"] / values["mass"])
        item_list.append(values['unit_cost'])

    # ----------------------find the lowest 'unit_cost'--------------- #
    # sort the list of unit costs
    item_list.sort()
    #set the remaining_budget
    remaining_budget = budget
    # then get the cheapest one and check if it's in the remaining_budget
    for cost in item_list:
        for name, values in items.items():
            # if it is then add it's name (do a reverse dictionary lookup) to a list called recomendation
            if values["unit_cost"] == cost and values["price"] <= remaining_budget:
                recomendation.append(name)

    print("I recomend you buy {}".format(recomendation))
# Give user option to restart or exit.
    restart = input("would you like to restart?   y/n:  ")
    if restart == "n": break
