#Ethan Anderson, John Lewis, and Israella Mayer
#EECE 346 - Probability and Statistics for Electrical and Computer Engineering
#Final Project
#Due: 6/13/2025

import random as rd
import matplotlib.pyplot as mpl
import numpy as np
import seaborn as sb
import scipy as sp

Samples = []
nValue = 0
Deviation = 0.0 
xBar = 0.0

tTable_90 = []
tTable_95 = []
tTable_99 = []


def User_Values():
    global Samples
    global nValue

    xValues = input("Enter the sample values, you can also enter just the sample mean for calculation: ")

    xValues = xValues.split(",")
    
    for i in xValues:
        Samples.append(float(i))

    for i in Samples:
        nValue += 1

    return Samples, nValue 

def Random_Values():
    global Samples
    global nValue

    nValue = rd.randint(1, 30)
    start = rd.randint(10, 1000)
    
    for i in range(nValue):
        num = start * rd.random()
        num = round(num, 4)
        Samples.append(num)

    random_float = rd.random()

    return Samples, nValue

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# print("Welcome to an auto confidence interval calculator\n" \
# f"This calculator takes in a set of sample values and outputs the mean confidence interval for the 90%, 95%, and 99% confidence intervals\n" \
# "You can input your own sample values, or have the calculator demontrate using randomly generated values\n")
Choice = input("If you want to use your own data, enter 'S'. If your want a demonstration with randomly generated values, enter 'R': ")

while True:
    if Choice == "S" or Choice == "s":
        User_Values()
        break

    elif Choice == "R" or Choice == "r":
        print("Demonstartion:")
        Random_Values()
        break

    else:
        Choice = input("Incorrect choice, please enter an 'S' for your own data or a 'R' for an randomly generated example: ")

if nValue == 1:
    xBar = Samples

else:
    Sum = np.sum(Samples)
    xBar = Sum/nValue
    xBar = round(xBar, 4)

print(f"{Samples}, {nValue}, {xBar}")