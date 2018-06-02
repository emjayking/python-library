# Date created: 29/05/18
# Author:Matthew King
# Version: 0.1
# What it does: An extended version of my Ai 'Queasito'. it uses back
# propagation to predict the outcome of simple statistical data.
# == == == == == == == == == == == == == == == == == == == == == == == #
import numpy as np # numpy is used in scientific calculations such
# as exponentials and nonlinear graphs (the sigmoid function -_-)

# This is how the code 'guesses' what the answer is. this is used later in
# the code. and also calculates the error from a sigmoid curve
# (when deriv == true) This is better than the origional Quaesito because
# it uses this function instead of doing the calculation on every line it
# is needed on


def nonlin(x, deriv=False):
    if deriv is True:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))


# input dataset (the questions)
x = np.array([[0, 0, 1],  # organising the array like this makes
              [0, 1, 1],  # it easier to read
              [1, 0, 1],  # the Ai will be given a variation of these
              [1, 1, 1]])  # and asked to calculate the output

# Output data set (the Answers)
y = np.array([[0, 0, 1, 1]]).T  # the '.T' makes the array verticle

# This means the Ai is given this
#  input 1  input 2  input 3  Answer
# [0,        0,       1]      [0]
# Question 2
# [0,        1,       1]      [0]
# Question 3
# [1,        0,       1]      [1]
# Question 4
# [1,        1,       1]      [1]

# The below code is copied directly from
# http://iamtrask.github.io/2015/07/12/basic-python-network/
# poor commenting is due to my own lack of understanding and will be updated
# over time
# --------------------------------------------------------------------------#

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initalise weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1,)) - 1

for iter in xrange(10000):

    # forward propagation (The Guess)
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss by?
    l1_error = y - l1
    # Figures out how much the quess was off by subtracting it from the
    # answer

    # Multiple how much we missed by the slope of the sigmoid at the
    # values in l1
    l1_delta = l1_error * nonlin(l1, True)  # by using the word 'True' it
    # activates the first branch of the if statement in the nonlin function
    # which takes the margin of error and multiplies it by a sigmoid curve to
    # figure out how much too adjust the weights by

    # Update (change) the weights
    syn0 += np.dot(l0.T, l1_delta)

# prints the codes final guess
print("output after training")
print(l1)
