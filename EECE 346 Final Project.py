#Ethan Anderson, John Lewis, and Israella Mayer
#EECE 346 - Probability and Statistics for Electrical and Computer Engineering
#Final Project
#Due: 6/13/2025

import random as rd
import matplotlib.pyplot as mpl
import numpy as np
import seaborn as sb
import scipy as sp
import math

Samples = []
nValue = 0
xBar = 0.0
Deviation = 0.0 
keys = ["C90", "C95", "C99"]
CritValue = {"C90": 0.0, "C95": 0.0, "C99": 0.0}
StandError = 0.0
MarginError = {"C90": 0.0, "C95": 0.0, "C99": 0.0}
tTable = {"C90": [
    6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812,
    1.796, 1.782, 1.771, 1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 
    1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703, 1.701, 1.699, 1.697
    ],
    "C95": [
    12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228,
    2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086,
    2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042
    ],
    "C99": [
    63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169,
    3.106, 3.055, 3.012, 2.977, 2.947, 2.921, 2.898, 2.878, 2.861, 2.845, 
    2.831, 2.819, 2.807, 2.797, 2.787, 2.779, 2.771, 2.763, 2.756, 2.750
    ]}


def User_Values():
    global Samples
    global nValue

    while(True):
        xValues = input("Enter the sample values: ")

        xValues = xValues.split(",")
        
        for i in xValues:
            Samples.append(float(i))

        for i in Samples:
            nValue += 1
        
        if nValue > 1:
            break

        else:
            print("Sample size must be 2 or more")

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

Sum = np.sum(Samples)
xBar = Sum/nValue
xBar = round(xBar, 4)

# Sample standard deviation {Samples and xBar}
for i in Samples:
    Deviation += (i * xBar) ** 2

Deviation = math.sqrt(Deviation)

# Critical value {nValue, tTable_90, tTable_95, and tTable_99}
for i in keys:
    CritValue[i] = tTable[i][nValue - 2]

# Standard error of the mean {Sample standard deviation and nValue}


# Margin of errors {Critical values and Standard error of the mean}


# Confidence intervals {xBar and Magin of errors} 

print(f"{Samples}, {nValue}, {xBar}, {Deviation}, {CritValue}, ")