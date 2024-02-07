import pandas as pd
import numpy as np
import math

data = pd.read_excel("C:\\Users\\eespl659\\Documents\\Learning\\ML\\Samples\\Icecream.xlsx")
df = pd.DataFrame(data)                     
x = df["Grams"]
y = df["Price"]



# x = [17,13,12,15,16,14,16,16,18,19]
# y = [94,73,59,80,93,85,66,79,77,91]


def mean(numbers):
    total_sum = sum(numbers)
    return total_sum / len(x)

def mean_diff(ls,mean):
    new_small = []
    for original in ls:
        new_value =  round(original - mean, 2)
        new_small.append(new_value)
    return new_small


def squared_numbers(squ):
    rounded_numbers = []
    squared_numbers = list(map(lambda x: x ** 2, squ))
    rounded_numbers = [round(num, 2) for num in squared_numbers]
    return rounded_numbers


mean_X = mean(x)
mean_Y = mean(y)

sux = mean_diff(x, mean_X)
suy = mean_diff(y, mean_Y)

suxx = squared_numbers(sux)
suyy = squared_numbers(suy)

L1 = np.array(sux)
L2 = np.array(suy)

Result = [round(numa, 2) for numa in L1*L2]

Sum_Result = sum(Result)

Sum_suxx = sum(suxx)
Sum_suyy = sum(suyy)

Value = Sum_suxx * Sum_suyy
square_root = math.sqrt(Value)

#Correlant Co-efficient
R = Sum_Result /square_root
#SD of Y
Dyy = len(y) - 1
SY = math.sqrt(Sum_suyy / Dyy)
#SD of X
Dyx = len(x) - 1
SX = math.sqrt(Sum_suxx / Dyx)
#Slope
m = R * (SY/SX)
Round_m = round(m, 2)

#Find C
c = mean_Y - (m * mean_X)
#Linear Reression
X = input("Please enter the Value: ")
Y = (float(Round_m) * float(X)) + c
print(Y)



   
