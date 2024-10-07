# Author: Paula Farebrother
# Created: Feb 2024
# Last modified: Oct 2024

# Pure python code to complete set tasks on a csv file.

import os
from datetime import datetime as dt

cwd = os.getcwd()
print("Current working directory is: ", cwd)
path = os.listdir(cwd)
print("Files available are: ", path)

with open("filename.csv", "r") as f: 

    def range(list_of_nums):
        """Calculates the range from a list of numbers."""
        range = max(list_of_nums) - min(list_of_nums)
        return range

    def mode(list_of_nums):
        """Calculates the mode for a list of numbers."""
        maxCount = (0, 0) # this sets a tuple
        for num in list_of_nums:
            occurences = list_of_nums.count(num)
            if occurences > maxCount[0]: # accesses the index of 0 in maxCount
                maxCount = (occurences, num)
        return maxCount[1] # This returns the num which is at index 1

    def mean(list_of_nums):
        """Calculates the mean from a list of numbers."""
        sumCol = 0
        for num in list_of_nums:
            sumCol += num
            mean = sumCol / len(list_of_nums)
        return round(mean, 2)

    def median(list_of_nums):
        """Calculates the median from a list of numbers.  Takes into account
            whether the total is odd or even."""
        list_of_nums.sort()
        if len(list_of_nums) % 2 != 0: # sets a case for odd number of items
            mid_index = int((len(list_of_nums) - 1) / 2) # ensures we go with 
            # integer not float to find num
            return list_of_nums[mid_index]
        elif len(list_of_nums) % 2 == 0: # sets a case for even number of items
            mid_index_1 = int(len(list_of_nums) / 2)
            mid_index_2 = int(len(list_of_nums) / 2) - 1
            return mean([list_of_nums[mid_index_1], list_of_nums[mid_index_2]])
          
    def convertUTC(list_of_nums):
        """Converts UTC timestamp to date and time."""
        dateFormat = []
        for num in list_of_nums:
            dateFormat.append(str(dt.fromtimestamp(num)))
        return dateFormat
    
    def access_row(col1, col2, col3):
        """Prints the correct date format next to the column values for
        the requested row for 3 column data files with timestamp."""
        row_no = int(input("Enter the row number you would like to see: "))
        print_row = "%1s" % (str(convertedUTC[row_no-1])) + "%10s" % (str(air_num[row_no-1])) + "%11s" % (str(cpu_num[row_no-1]))
        # converting to string removes the parenthesis from displayed result
        print("%12s" % (col1), "%15s" %(col2), "%10s" % (col3))
        return print_row
    
    """With dataset open, code counts and outputs the total number of rows."""

    theSum = 0
    for line in f:
        theSum += 1
         
    print("There are", theSum, "rows in this dataset.")
    print("There are", theSum - 1, "rows of data in this dataset.")

with open("tempLog.csv", "r") as f: # total records only works with file reopened.

    records = []
    """Creates an individual list within a list of each of the records 
        for each row in the same order as in the data file."""    

    for line in f:
        rcrd = line.split(",")
        records.append(rcrd)
        total = len(records) * 3 # the number of columns
    print("The number of records in this file (excluding headers) is: ")
    print(total - 3) # excludes headers
           
    # There are 3 columns so we can access columns to further analyse data.
    
    timestamp = []
    air = []
    cpu1 = []
    cpu = []
    for record in records:
        timestamp.append(record[0])
        air.append(record[1])
        cpu1.append(record[2])
        cpu = [i.strip("\n") for i in cpu1]
    
    # Next I need to remove the title from each column 

    timestamp.pop(0)
    air.pop(0)
    cpu.pop(0)

    # then transform the data into numerical entries

    timestamp_num = [eval(i) for i in timestamp]
    air_num = [float(i) for i in air]
    cpu_num = [float(i) for i in cpu]

#________Now the data is ready to be analysed_________________________________    

    # Scale data using block code not function
    # Scale data using calculation Xnew = X - Xmin / Xmax - Xmin
    # I've had to move scale before IQR as it was altering my scale results
    # but I'm not sure why yet.

    air_mins = []
    for i in air_num:
        air_min = float(i) - min(air_num)
        air_mins.append(round(float(air_min), 2))
    
    maxMin = round((max(air_num) - min(air_num)), 2)
    
    # Complete the equation iterating through each item

    scaled = []

    for i in air_mins:
        scaledi = i / maxMin
        scaled.append(round(scaledi, 2))
    print("These are the scale values for Air: ")
    print("Row 136: ", scaled[137]) # allows for off by one error
    print("Row 2460: ", scaled[2461]) # allows for off by one error

    cpu_mins = []
    for i in cpu_num:
        cpu_min = float(i) - min(cpu_num)
        cpu_mins.append(round(float(cpu_min), 2))

    maxMin = round((max(cpu_num) - min(cpu_num)), 2)

    # Complete the equation iterating through each item

    scaled = []

    for i in cpu_mins:
        scaledi = i / maxMin
        scaled.append(round(scaledi, 2))
    print("These are the scale values for CPU: ")
    print("Row 1590: ", scaled[1591]) # allows for off by one error
    print("Row 4950: ", scaled[4951]) # allows for off by one error
#______________________________________________________________________________
    # IQR has not yet been converted to a function so I will calculate this first
    # This example shows how much information is created if you are not using
    # code blocks.
    # First for Air column
    
    middle = median(air_num) # this is the value in the middle, not index value

    # need to sort list first
    air_num_ord = sorted(air_num)
    cpu_num_ord = sorted(cpu_num)

    middle_index = 0
    if len(air_num_ord) % 2 != 0: # sets a case for odd number of items
        mid_index = int((len(air_num_ord) - 1) / 2) # ensures we go with 
        # integer not float to find num
        middle_index += mid_index
    elif len(air_num_ord) % 2 == 0: # sets a case for even number of items
        mid_index_1 = int(len(air_num_ord) / 2) - 1 # for odd data set we omit the
        # central median
        middle_index += mid_index_1

    # next we calculate median index for upper and lower sections of data set
    
    lowerQuart = air_num_ord[0:middle_index]    
    upperQuart = air_num_ord[middle_index:]

    # median of the lower quartile needed now
    q1 = median(lowerQuart) # I haven't rounded here as I think it will skew the results
    q3 = median(upperQuart)

    iqr = q3 - q1 # The difference between the upper and lower quartile medians
    print("The IQR for air is: ", round(iqr, 2)) 

    # Next for CPU column
    
    middle = median(cpu_num) # this is the value in the middle, not index value

    # need to sort list first
    air_num_ord = sorted(cpu_num)

    middle_index = 0
    if len(cpu_num_ord) % 2 != 0: # sets a case for odd number of items
        mid_index = int((len(cpu_num_ord) - 1) / 2) # ensures we go with 
        # integer not float to find num
        middle_index += mid_index
    elif len(cpu_num_ord) % 2 == 0: # sets a case for even number of items
        mid_index_1 = int(len(cpu_num_ord) / 2) - 1 # for odd data set we omit the
        # central median
        middle_index += mid_index_1

    # next we calculate median index for upper and lower sections of data set
    
    lowerQuart = cpu_num_ord[0:middle_index]
    upperQuart = cpu_num_ord[middle_index:]
    
    # median of the lower quartile needed now

    q1 = median(lowerQuart) # I haven't rounded here as I think it will skew the results
    q3 = median(upperQuart)

    iqr = q3 - q1 # The difference between the upper and lower quartile medians
    print("The IQR for CPU is: ", round(iqr, 2)) 

#_______________ functions ___________________________________________________
    # These examples show how much more efficient the code is using functions
    # compared to blocks of code.  It is much easier to problem solve functions
    # than blocks of code, and much more readable and easier to understand
    # what the code is doing.

    # Calculate the mean

    print("This is the mean for air: ", mean(air_num))
    print("This is the mean for cpu: ", mean(cpu_num))

    # Calculate the median (most often occuring figure)
     
    print("This is the median for air: ", median(air_num))
    print("This is the median for cpu: ", median(cpu_num))

    # Calculate the mode

    print("This is the mode for air: ", mode(air_num))
    print("This is the mode for cpu: ", mode(cpu_num))

    # Cacluate minimum and maximum 

    print("This is the minimum for air: ", min(air_num)) 
    print("This is the maximum for air: ", max(air_num)) 
    print("This is the minimum for CPU: ", min(cpu_num))
    print("This is the maximum for CPU: ", max(cpu_num))

    # Calculate range

    print("This is the range for air: ", range(air_num))
    print("This is the range for CPU: ", range(cpu_num))

    # Convert timestamp into date format
   
    convertedUTC = convertUTC(timestamp_num)
    
    # User input row selector

    print(access_row("timestamp", "air", "cpu"))

    # End of code
