"""goal: output the collatz conjecture of a specific number and report its rainfall numbers""" 
import matplotlib.pyplot as plt

integer = input("Please input a positive integer ")
def collatz(n):
    yAxisList = [n]
    while n != 1:
        if n < 1:
            raise Exception("Please enter an integer greater than 1")
        elif n % 2 == 0: 
            n = n/2
            yAxisList.append(n)
            print(yAxisList)
        elif n % 2 != 0: 
            n = 3*n+1
            yAxisList.append(n)
            print(yAxisList)
    xAxisLength = len(yAxisList) # including the inputted number
    print(f"length: {xAxisLength-1}")
    xAxisNum = list(range(1, xAxisLength+1))
    plt.plot(xAxisNum,yAxisList)
    plt.show()

try:
    integerO = int(integer)
except:
    print("please input a valid integer")
else:
    collatz(integerO)
