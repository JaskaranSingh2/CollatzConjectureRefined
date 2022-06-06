"""
This script will attempt to integrate 9999 integers (2-10000, as n != 1) and attempt to derive
some sort of pattern with the stopping time (as in, the total number of iterations before natRange = 1) of each integer.
"""

import matplotlib.pyplot as plt
def CollatzNat(natRange): # natRange is replaced with natRangeIteration to test all 10000 numbers
    outputListY = [natRange] # Includes the number iterated into natRange as first number of outputListY
    while natRange != 1:
        
        if natRange % 2 == 0:
            natRange = natRange / 2
            outputListY.append(natRange)
            
        elif natRange % 2 > 0:
            natRange = (3*natRange)+1
            outputListY.append(natRange)
            
    print(f"Collatz Conjecture of [{natRangeIteration}, including the tested number: {outputListY}") # To make sure all iterations of 'natRangeIteration' are tested
    return(outputListY) # Exits function, reports the list (outputListY) as the "value" of the function

# (l.23,24) are scales for the graph, appended in for loop after...
x=[]
y=[]

for natRangeIteration in range(1, 10001):  # In math terms: [1,10001).
    # Self-note: Is this calling the function? If I remove this it won't print (l. 19)
    returnedNatValue = CollatzNat(natRangeIteration) 
    # CollatzNat(natRangeIteration) returns outputListY over each iteration and stores the list into returnedNatValue
    # The value of returnedNatValue gets rewritten everytime, which makes sense, as this is a for loop.

    x.append(natRangeIteration) # for each iteration ('natRangeIteration'), the list is appended to include the number being tested
    
    # Stopping time of a number (arithmetic steps). Takes length of list [returned value of called function (l.20)], then convert into a number list 
    y.append(len(returnedNatValue)-1) 
    # One is subtracted because we had included the tested number 'natRangeIteration' in the list, so the stopping time is (list-1)

print(f"The stopping time for each tested number: {y}") # Prints the stopping time for each number, just for good measure
plt.plot(x,y, "o")
plt.xlabel('Integers 2-10000')
plt.ylabel('Number of arithmetic steps before reaching 1')
plt.title('Number of Iterations / Arithmetic steps per integer in the Collatz Conjecture')
plt.show()