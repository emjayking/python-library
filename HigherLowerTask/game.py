# Date created: 5/06/18
# Author:Matthew King
# Version: 2.0
# What it does: Simple game based on instructions given in the
# word document found in the folder. fully unbreakable complete with
# flexible start and stop numbers and line by line commenting
# == == == == == == == == == == == == == == == == == == == == == == == #
# imports
import random  # used for random number generation
import time  # used to fill out if statements
# variables
cont = 'yes'  # weather or not the user wants to continue

scores = []  # list of user scores (how long it took them to guess the answer)

rounds_played = 0  # how many rounds the user has played
# definitions


def force_num(message):  # a function used to force the user to enter a valid number
  while True:
    try:
      number = int(input(message))
      break
    except ValueError:
      print("please enter a valid number!")
  return number


# function used to check if a value is within certain boundary values.
def is_reasonable(variable, max=1000, min=0):
  if variable > max or variable < min:
    print("Please choose a more reasonable number")
    reasonable = False
  else:
    print("Good Choice")
    reasonable = True
  return reasonable


# --------------------------- Start of code---------------------#

while cont == 'yes':  # while the user wants to continue
  # Generate secret number
  while True:
    # ask the user for the smallest possible random number
    start = force_num("Enter the minimum value for the random number:  ")
    # check that the number isnt stupid
    start_okay = is_reasonable(start, 500)
    if start_okay is True:  # if the number isn't stupid then move on
      time.sleep(0.1)

    else:  # if the number is stupid then skip the rest of
      # the loop and start again
      continue
    # the largest number the random number can be
    end = force_num("Enter the maximum value for the random number:  ")
    # check the number isn't stupid
    end_okay = is_reasonable(end, start)
    # if it's not stupid, exit the loop
    if end_okay is True:
      time.sleep(0.1)
      break
    # if it is stupid then start all over again
    else:
      continue
  # calculate the random number based on the minimum and maximum
  # values answer = random.randint(start, end)
  answer = random.randint(start, stop)
  # how many guesses would the user like?
  while True:
    guesses = force_num("How many guesses would you like?")
    # check if the number isn't larger than the number of possible guesses
    guesses_okay = is_reasonable(guesses, 0, end - start)
    # if it is, loop again
    if guesses_okay is False:
      time.sleep(0.1)
    # if it's fine, stop the loop
    else:
      break

  # ask the user to guess the number
  for i in range(10):
    guess = force_num(
        "please enter a number between {} and and {}:  ".format(start, end))
    # if the guess is inside the number possible answers
    if guess >= start and guess <= end:
      # then check if the user gets it right
      if guess == answer:
        # tell the user they got it right, on what turn
        # they got it right and what the answer was
        print("You guessed it on try number {}."
              " well done, the number was {}"
              .format(i + 1, answer))
        break  # then stop checking
      # otherwise if the guess was higher than the answer
      elif guess > answer:
        # tell the user to guess lower and how many tries they have left
        print("Lower,"
              " you have {} trys remaining"
              .format(10 - (i + 1)))
      # if it's not the answe rand its not higher than the
      # answer it must be lower than the answer so
      else:
        # tell the user to guess higher and how many tries they have left
        print("Higher,"
              " you have {} trys remaining".format(10 - (i + 1)))
    # the guess must be either larger or smaller than the
    # possible answers, so start again
    else:
      print("That guess wasn't between {} and {}. try again!"
            " you have {} trys ramaining".format(start, end, 10 - (i + 1)))
  # if the user used up all 10 of their tries (i is always 1 less than the actuall number of times looped in a for loop)
  if i == 9:
    # tell the user what the answer was
    print("You Failed! the answer was {}".format(answer))
  else:  # ifs must have an else. this is a good way to do that
    # with minimal code impact
    time.sleep(0.1)

  # ask the user if the would like to play again.
  cont = input("would you like to play again?,"
               " type 'yes' or 'no'  ").strip().lower()
  # add this round to the total number of rounds played
  rounds_played += 1
  # add the score to the list of scores
  scores.append(i)
# when the user is done print out some summary statistics
print("You played {} rounds. your best score was {}. your worst score was {}".format(
      rounds_played, min(scores), max(scores)))  # the minimum score will be
# whatever round they took the least amount turns to guess the answer
# aka their best round, vice versa with the maximum number
