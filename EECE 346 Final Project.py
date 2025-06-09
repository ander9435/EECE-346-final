#Ethan Anderson, John Lewis, and Israella Mayer
#EECE 346 - Probability and Statistics for Electrical and Computer Engineering
#Final Project
#Due: 6/13/2025

import random as rd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from scipy.stats import t
import math

Samples = []
nValue = 0
xBar = 0.0
Deviation = 0.0 
keys = ["CI_90", "CI_95", "CI_99"]
CritValue = {"CI_90": 0.0, "CI_95": 0.0, "CI_99": 0.0}
StandError = 0.0
MarginError = {"CI_90": 0.0, "CI_95": 0.0, "CI_99": 0.0}

tTable = {"CI_90": [
    6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812,
    1.796, 1.782, 1.771, 1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 
    1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703, 1.701, 1.699, 1.697
    ],
    "CI_95": [
    12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228,
    2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086,
    2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042
    ],
    "CI_99": [
    63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169,
    3.106, 3.055, 3.012, 2.977, 2.947, 2.921, 2.898, 2.878, 2.861, 2.845, 
    2.831, 2.819, 2.807, 2.797, 2.787, 2.779, 2.771, 2.763, 2.756, 2.750
    ]}

#Data must be of datatype np.array and ci and exmean are integers. 
def GraphGeneration(): 

    # Plot the Gaussian (normal) distribution
    x_vals = np.linspace(xBar - 3*Deviation, xBar + 3*Deviation, 300)
    pdf = t.pdf(x_vals, nValue - 1, xBar, Deviation)

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, pdf, label='T Distribution', color='gray')

    # Fill the 90% confidence interval
    plt.axvline(xBar-MarginError["CI_90"], color='purple', linestyle='--', label=f'90% CI')
    plt.axvline(xBar+MarginError["CI_90"], color='purple', linestyle='--')
    plt.fill_between(x_vals, 0, pdf, where=(x_vals >= xBar-MarginError["CI_90"]) & (x_vals <= xBar+MarginError["CI_90"]), color='purple', alpha=0.2)

    # Fill the 95% confidence interval
    plt.axvline(xBar-MarginError["CI_95"], color='blue', linestyle='--', label=f'95% CI')
    plt.axvline(xBar+MarginError["CI_95"], color='blue', linestyle='--')
    plt.fill_between(x_vals, 0, pdf, where=(x_vals >= xBar-MarginError["CI_95"]) & (x_vals <= xBar+MarginError["CI_95"]), color='blue', alpha=0.2)

    # Fill the 99% confidence interval
    plt.axvline(xBar-MarginError["CI_99"], color='red', linestyle='--', label=f'99% CI')
    plt.axvline(xBar+MarginError["CI_99"], color='red', linestyle='--')
    plt.fill_between(x_vals, 0, pdf, where=(x_vals >= xBar-MarginError["CI_99"]) & (x_vals <= xBar+MarginError["CI_99"]), color='purple', alpha=0.2)


    # Expected and Sample means
    plt.axvline(xBar, color='black', linestyle='-', label='Sample Mean')

    # Labels and legend
    plt.title(f"Sample Mean, Confidence Interval and Fitted Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)
    plt.show()

def User_Values():
    global Samples
    global nValue

    while(True):
        xValues = input("Enter the sample values, seperate values with a comma: ")

        xValues = xValues.split(",")
        
        for i in xValues:
            Samples.append(float(i))

        for i in Samples:
            nValue += 1
        
        if nValue > 1:
            break

        else:
            print("Sample size must be 2 or more")
    
    print("\nFinal Data:")

    return Samples, nValue 

def Random_Values():
    global Samples
    global nValue

    nValue = rd.randint(10, 30)
    mean = rd.randint(0, 50)
    sd = rd.randint(1, 5)

    Samples = np.random.normal(mean, sd, nValue)

    return Samples, nValue

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Welcome to an auto confidence interval calculator\n" \
f"This calculator takes in a set of sample values and outputs the mean confidence interval for the 90%, 95%, and 99% confidence intervals\n" \
"You can input your own sample values, or have the calculator demontrate using randomly generated values.\n")
Choice = input("If you want to use your own data, enter 'S'. If your want a demonstration with randomly generated values, enter 'R': ")

while True:
    if Choice == "S" or Choice == "s":
        User_Values()
        break

    elif Choice == "R" or Choice == "r":
        print("\nDemonstartion:")
        Random_Values()
        break

    else:
        Choice = input("Incorrect choice, please enter an 'S' for your own data or a 'R' for an randomly generated example: ")

# Sample mean {Samples and nValue}
Sum = np.sum(Samples)
xBar = Sum/nValue
xBar = round(xBar, 4)

# Sample standard deviation {Samples and xBar}
for i in Samples:
    Deviation += (i - xBar) ** 2

Deviation = (math.sqrt(Deviation / (nValue - 1)))

# Critical value {nValue, tTable_90, tTable_95, and tTable_99}
for i in keys:
    CritValue[i] = tTable[i][nValue - 2]

# Standard error of the mean {Sample standard deviation and nValue}
    StandError = Deviation / math.sqrt(nValue)

# Margin of errors {Critical values and Standard error of the mean}
    for i in keys:
        MarginError[i] = CritValue[i] * StandError

print(f"  Sample List: {Samples}\n  Sample Size: {nValue}\n  Sample Mean: {xBar}\n  Standard Deviation: {Deviation}\n  Critical Values: {CritValue}\n  Margin Error: {MarginError}")

GraphGeneration()