# Author: Paula Farebrother
# Created: Feb 2024
# Last modified: Oct 2024

# This module uses NumPy to open, read and analyse data within a csv file.

import numpy as np

my_array = np.loadtxt("filename.csv", delimiter = ",", skiprows= 1)
print(my_array)

print(my_array.shape) # shows number of rows and columns
print(my_array.size) # shows the number of records (including timestamp)

timestamp = my_array[ :,0] # creates timestamp column
air = my_array[ :,1] # creates air column
cpu = my_array[ :,2] # creates cpu column

# IQR

q75, q25 = np.percentile(air, [75 ,25])
iqr = q75 - q25
print("This is the IQR for Air: ", iqr)

q75, q25 = np.percentile(cpu, [75, 25])
iqr = q75 - q25
print("This is the IQR for CPU: ", iqr)

# Scale function not available

# Mean

print("This is the mean of Air: ", np.mean(air))
print("This is the mean of CPU: ", np.mean(cpu))

# Median

print("This is the median of Air: ", np.median(air))
print("This is the median of CPU: ", np.median(cpu))

# Mode function not available

# Min and Max values 

print("This is the minimum value of air: ", np.min(air))
print("This is the maximum value of air: ", np.max(air))

print("This is the minimum value of CPU: ", np.min(cpu))
print("This is the maximum value of CPU: ", np.max(cpu))

# range not available

# correlation coefficient of array

print("Correlation Coefficient for Air and CPU: ", np.corrcoef(air, cpu)) # displays correlation coeffecient between variables
