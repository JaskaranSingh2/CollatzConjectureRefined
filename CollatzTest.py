# Basic self-inputter to brute test numbers

import matplotlib.pyplot as plt
posInt = input("Input a positive integer --> ")
outputListY = [int(posInt)]

# Try and exception, to make sure that the input is valid
try: 
    y=int(posInt)
except:
    print("Please type in a valid positive integer!")
else: 
    if y < 0:
        raise Exception("only positive integers!")
    while y != 1:
        if y % 2 == 0:
            y = y / 2
            outputListY.append(y)
            print(outputListY)
        elif y % 2 > 0:
            y = (3*y)+1
            outputListY.append(y)
            print(outputListY)
lengthOfXNumbered = len(outputListY) # the length of this (including the inputted number) is used in (l. 35) to convert a range into a list, to put on the x-axis. 
adjustedNumberOfXNumbered = lengthOfXNumbered-1 # adjustedNumberOfXNumbered is the total number of terms / arithmetic steps, excluding the inputted number, hence subtracting 1.
print(f"This is the total number of arithmetic steps / terms, excluding the number inputted: {adjustedNumberOfXNumbered}")


# To graph it:

""" 
Printed out to the user: This is the list that will be put on the x-axis, including the inputted number as the first iteration (n, n∈I+)
We add one to "lengthOfXNumbered" in (l. 35), because we want the list to start at 1. -> (l.33,34)
"""
xScaleList = list(range(1, lengthOfXNumbered+1))
print(f"List that will be put on the x-axis, including the inputted number ('n') as the first iteration (n, n∈I+) [(x,n) -> (1,n)]: {xScaleList}")

plt.plot(xScaleList, outputListY)
plt.xlabel("Iterations over arithmetic rules for 'n', where n∈I+. The inputted number ('n') is recorded as the first iteration")
plt.ylabel("value of 'n' after arithmetic steps before n (natRange) = 1")
plt.title("Collatz Conjecture for said integer. Note: Number inputted ('n') is plotted as first iteration, so the x-axis does not record the exact number of steps in the conjecture, see (l. 25,26)")
plt.show()
