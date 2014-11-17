# Principles of Urban Informatics
# Assignment 4
# Problem 1
#
# check your own code before you benchmark it:
# does it actually compute unique lists?
# 
# by brigitte.jellinek@nyu.edu
#

from problem1 import solveOnlyLists, solveDict, solveSorted

import random
import math
    

def solveWithSet(inputList):
    outputSet = set(inputList)
    return list(outputSet)


def generateSampleInput(inputSize,isSorted=False):
    sampleInput = []
    for i in xrange(inputSize):
        sampleInput.append(random.randint(0,100))
    if isSorted:
        sampleInput.sort()
    return sampleInput


functionsToTest = [solveOnlyLists, solveDict, solveSorted]
data = generateSampleInput(10)

correct_solution = solveWithSet(data)
for func in functionsToTest:
    print 'Testing %s()' % func.__name__
    if func.__name__ == "solveSorted":
      this_solution = func(sorted(data))
    else: 
      this_solution = func(data)

    if set(correct_solution) == set(this_solution):
      print "OK"
    else:
      print "ERROR, %s() does not do it's job correctly!" % func.__name__
      print correct_solution
      print "wrong solution:"
      print this_solution