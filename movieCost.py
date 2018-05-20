# Date created: 16/05/18
# Author:Matthew King
# Version: 0.1
# What it does:calculates the cost of people buying movie tickets
# and then adds a discount if appropriate. is fully unbreakable
# but only has limited price range

# == == == == == == == == == == == == == == == == == == == == == == == #
# variables
prices = [5, 10, 15, 20]
# functions


def tickets(people, cost):
    # calculate cost
    total_cost = cost * people
    print("your total cost is ${}".format(total_cost))
    # if people > 8 calc discount
    if people >= 8:
        total_cost -= total_cost * 0.15
        print("you have more than 8 people in your group so you get a 15"
              "%  discount. so your total cost is {}".format(total_cost))
    else:
        print("you are not eligible for a discount")

    # return total cost
    return total_cost


def force_num(message, errorMessage):
    # forces the user to enter a number so the code won't break
    while True:
        try:
            number = int(input(message))
            if number > 0 and number != 0:
                break
            else:
                print(errorMessage)
        except ValueError:
            print(errorMessage)
    return number


def cost():  # forces the user to choose a price from a list
    while True:
        try:
            cost = int(
                input("please choose a price from the list,"
                      " $5, 10, $15, $20.   $"))
            if cost in prices:  # better than a ton of elif statements
                print("awesome! good choice. enjoy the show!")
                break
            else:
                print("sorry that price is not available")
        except ValueError:
            print("please enter a valid number (dont use the dollar sign)")
    return cost


# number of people
num_people = force_num("How many people are in your group?",
                       " Sorry, I didn't get that")
# price of tickets
cost_per_ticket = cost()
# calculate cost
total_cost = tickets(num_people, cost_per_ticket)

# print final messages
if num_people > 8:
    print("awesome so, you are a group of {} people purchasing"
          " ${} dollar tickets. you get a 15%  discount so your final"
          " price is ${}".format(num_people, cost_per_ticket, total_cost))
