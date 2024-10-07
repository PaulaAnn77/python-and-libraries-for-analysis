# Author: Paula Farebrother
# Created: Feb 2024
# Last modified: Oct 2024

# Using the imported reference library Pandas to complete set tasks on csv file.

import pandas as pd

df = pd.read_csv("filename.csv") # reads the csv file

# Count the number of rows and columns

print("Rows and columns respectively are", df.shape) 

# set columns to variables

timestamp = df.iloc[:, [0]]
air = df.iloc[:, [1]]
cpu = df.iloc[:, [2]]


total_entries = len(timestamp) + len(air) + len(cpu)
print("The total data entries: ", total_entries) 
# includes timestamp column

# Print descriptive stats

print(df.describe()) # provides descriptive statistics for the data set

# iqr - there is no requirement to sort data first when using quantile in Pandas

q1_air = air.quantile(0.25)
q3_air = air.quantile(0.75)
iqr_air = q3_air - q1_air
print("The IQR for", iqr_air)

q1_cpu = cpu.quantile(0.25)
q3_cpu = cpu.quantile(0.75)
iqr_cpu = q3_cpu - q1_cpu
print("The IQR for", iqr_cpu)

# Scale data (indexing starts at 0)

print("This is index 2: ", df.iloc[1])
scaled_air = (air.iloc[137]-air.min())/(air.max()-air.min())
print("Scale value for Air, row 136: ", scaled_air)
scaled_air = (air.iloc[2461]-air.min())/(air.max()-air.min())
print("Scale value for Air, row 2460: ", scaled_air)

scaled_cpu = (cpu.iloc[1591]-cpu.min())/(cpu.max()-cpu.min())
print("Scale value for CPU, row 1590: ", scaled_cpu)
scaled_cpu = (cpu.iloc[4951]-cpu.min())/(cpu.max()-cpu.min())
print("Scale value for Air, row 4950: ", scaled_cpu)

# Median

print("This is the median for", air.median())
print("This is the median for", cpu.median())

# Mode

print("This is the mode for: ", air.mode())
print("This is the mode for: ", cpu.mode())

# Range

print("This is the range for Air: ", air.max() - air.min())
print("This is the range for CPU: ", cpu.max() - cpu.min())




