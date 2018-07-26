# Date created: 22/06/18
# Author:Matthew King
# Version: 1.0
# What it does: calculates the total amount of time a user
# spends gaming then gives them feedback on it
# == == == == == == == == == == == == == == == == == == == == == == == #
# Variables
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
timeList = []
totalTime = 0

# functions

# function that forces the user to enter a valid number.
# used to make sure the user doesn't enter strings or floats
# into the timeSpent variable which would cause a crash


def force_num(message):
    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            print("please enter a valid number!")
    return number

# function that forces the user to enter a valid word.
# used to make the user enter an actual name


def force_word(message):
    while True:
        try:
            word = str(input(message))
            break
        except ValueError:
            print("please enter a valid word!")
    return word


# ask for users name.
while True:  # infinite loop that forces the user to enter an input
    # using the force word function to force the user to enter a string
    name = force_word("What is your name?")
    if name.isalpha() is False:  # if it somehow fails then this is the backup
        print("please dont use numbers!")
    else:
        break  # but if the user enters an actual name the exit the infi loop
print("{} is a nice name!".format(name.capitalize()))  # worthless compliments

# start loop
for i in range(7):
    # ask the user how much time they spend gaming each day
    while True:  # for each day of the week
        timeSpent = force_num(  # ask the how much time they spent on each day
            "How many hours (whole numbers only) did you"
            " spend gaming on {}, {}?"
            .format(days[i], name))
        # check the user didn't enter anything stupid
        if timeSpent > 24 or timeSpent < 0:
            print("LIAR")  # if the did then call them out
        # if the time spent is above the recomeneded
        elif timeSpent > 2:
            print("Hmm bit more than recomended")  # being judgey
            break
        # if not it must be below recomended
        else:
            print("Good Job")  # commend their efforts
            break
    # print(i) (used for bug fixing)
    # add to list
    timeList.append([i, timeSpent])
    # list of all the total times, used to find the min and max values
    totalTime += timeSpent  # the total time spent, used to find average
# print(timeList) (used for bug fixing)
# print(timeSpent) (used for bug fixing)

# ----------------------------calculations--------------------------

# min time
minTime = min(timeList)
print("The least amount of time you spent gaming in one day was {} hours"
      .format(minTime[1]))
# max time
maxTime = max(timeList)
print("the most amount of time you spent gaming in one day was {} hours"
      .format(maxTime[1]))
# average time
averageTime = totalTime / 7
print("The average amount of time you spent gaming each day was {:.2f} hours"
      .format(averageTime))

# if average time > 2 , scold them
if averageTime > 2:
    print("Not good enough {}. some old guy who is important"
          " recomends that you have to spend only 2 hours per day on tech."
          " so you should cut back by {} hours per day. okay? "
          .format(name, averageTime - 2))

# otherwise congratulate them
else:
    print("well done {}, you are under the recomended amount of"
          " time spent gaming each day. good for you".format(name))
