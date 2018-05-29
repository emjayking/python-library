# Date created: 29/05/18
# Author:Matthew King
# Version: 0.1
# What it does: simple AI that uses back propogation to guess outputs of 1
# and 0 combinations.
# == == == == == == == == == == == == == == == == == == == == == == == #
import numpy as np  # shortens it to save space

# Arrays (example inputs and answers)
# Inputs (Questions)
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# Answers
Y = np.array([[0, 1, 1, 0]]).T  # the '.T' makes the array verticle

# synnapses (Things that join the neurons (arrays) together)
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

# The CODE
for j in range(60000):
    l1 = 1 / (1 + np.exp(- (np.dot(X, syn0))))  # guess 1
    l2 = 1 / (1 + np.exp(- (np.dot(l1, syn1))))  # guess 2
    l2_delta = (Y - l2) * (l2 * (1 - l2))  # Error of guess 2
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))  # Error of guess 1
    syn1 += l1.T.dot(l2_delta)  # Adjust the synapses by the error
    syn0 += X.T.dot(l1_delta)  # Adjust the synapeses by the error
