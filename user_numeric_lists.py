"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math
import statistics


list = ['Breathing Excercise','cobra pose','Tree Pose','Triangle Pose','Plant Pose','Pranayama','Yamas','Niyamas','Bridge Pose']
list1 = [12,15,18,21,24,27,30,33,36,39,41,44,47,49,49,49,50,51,53,55,57,59,61,64,66,69,70,73,75]
listx = []
listy = [100.2,121.4,134.5,132.3,143.7,152.8,157.8,163.1,178.5,184.2]

for number in range(10):
    listx += [number]
print('listx representing 10 integer:', listx)

list1[4] = 23
print('list1 after modifications:',list1)

print('Ages of students in yoga Institute:',listy)

# Descriptive: Averages and measures of central tendency
# Use statisttics module to get mean, median, mode
# for a values list

mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)

print('mean of list1:', mean)
print('median of list1:', median)
print('mode of list1:', mode)

# Descriptive: Measures of spread
# Get standard deviation and variance for a values list

stdev = statistics.stdev(list1)
variance = statistics.variance(list1)

print('Standard Deviation of list1:', stdev)
print('Variance of list1:', variance)

# Descriptive: Measures of correlation
# Use two numerical lists of the same size
# Use statisttics module to get correlation between listx and listy

correlationxy = statistics.correlation(listx,listy)

print('Correlation between listx and listy:', correlationxy)

# Predictive: Machine Learning - Linear Regression
# If the corrlation is close to 1.0, then the data is linearly related
# If so, use statistics module to get linear regression for list1 and list2
# This is a form of supervised machine learning - it uses all known data
# Use the slope and intercept and an unknown (future) x to predict a y value
# Python functions can return multiple values

slope, intercept = statistics.linear_regression(listx,listy)

print(f'Slope: {slope:.3f}')
print(f'Intercept: {intercept:.3f}')

# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

futute_x = 15

future_y = slope*futute_x + intercept

print(f'the future vale: {future_y:.4f}')

# BUILT-IN FUNCTIONS ......................................
# Many built-in functions work on lists
# try min(), max(), len(), sum(), sorted(), reversed()

# Using the score list provided above, do the following:
# Calcuate the max and min scores

max = max(listy)
min = min(listy)

print('list1 values max and min:', max , min)

# Calculate the length of the list
len = len(list1)

print('list1 values length:',len)

# Calculate the sum of the list
sum = sum(list1)

print('list1 values sum:',sum)

# Calculate the average of the list
avg = sum / len

print('list1 values average:',avg)

# Return a new list soreted in ascending order
asc_scores = sorted(listy)

print('listy values in ascending order:',asc_scores)

# Return a new list soreted in descending order
desc_scores = sorted(listy, reverse=True)

print('listy values in descending order:',desc_scores)

"""
LIST METHODS ............................................... 
Here are some common methods that operate on an instance of a list.
append(x): Add an item to the end of the list.
extend(iterable): Add all the items from an iterable (such as another list)
     to the end of the list.
insert(i, x): Insert an item at a given position.
remove(x): Remove the first occurrence of an item.
pop([i]): Remove the item at the given position in the list, 
    and return it. If no index is specified, 
    removes and returns the last item in the list.
clear(): Remove all items from the list.
index(x[, start[, end]]): Return the index of the first occurrence of
     an item.
count(x): Return the number of occurrences of an item.
sort(key=None, reverse=False): Sort the items in the list 
     in ascending order.
reverse(): Reverse the order of the items in the list.
copy(): Return a shallow copy of the list.
"""

# append an item to the end of the list
list1.append(77)

# extend the list with another list
list1.extend([78, 79, 80])

# insert an item at a given position (0 = first item)
i = 9
newvalue = 42
list1.insert(i, newvalue)

# remove an item
item_to_remove = 61
list1.remove(item_to_remove)

print('list1 values after performing some operations:', list1)

# Count how many times 49 appears in the list
ct_of_49 = list1.count(49)

print('49 value in list1:',ct_of_49,'times')

# Sort the list in ascending order using the sort() method
asc_scores2 = list1.sort()

print('list1 values in ascending order:',asc_scores2)

# Sort the list in descending order using the sort() method
desc_scores2 = list1.sort(reverse=True)

print('list1 values in descending order:',desc_scores2)

# Copy the list to a new list
new_scores = list1.copy()

# Remove the first item from the new list
# The first item in a list is at index 0
# Think of it as an offset from the beginning of the list
first = new_scores.pop(0)

# Remove the last item from the new list
# The last item in a list is at index -1
last = new_scores.pop(-1)


print('Values after removing first and last values form list1:',new_scores)



# TRANFORMATIONS ............................

# FILTER and MAP are critical in big data applications

# Use the built-in function filter() anywhere you need to filter a list
# Filter the new list to only include scores greater than 100
# You could pass in a named function, but honestly this is easier
# Say "keep x such that x > 100 is True" given new_scores
# Cast the result using square brackets to get a list
scores_over_50 = [filter(lambda x: x > 50, new_scores)]

print('list1 values over 50:',scores_over_50)

# Use the built-in function map() anywhere you need to transfrom

# Map each element to its cube
# Cast the result using square brackets to get a list
cube_scores = [map(lambda x: x ** 3, new_scores)]

print('cube values:',cube_scores)

# Map each element to its cube root
# Say "map x to the cube root of x" and cast to a list
cbrt_scores = map(lambda x: math.cbrt(x), new_scores)

print('cube root values:',cbrt_scores)

# volume of a cube 
vol_list = [map(lambda s: s*s*s, list1)]

print('voulume of the cube:',vol_list)


# TRANFORMATIONS - Using List Comprehensions
# List comprehensions are a concise way to create lists
# They work like map and filter, but are more concise
# They are the preferred "pythonic" way to do transformations

# With comprehensions, we start with what we WANT
# Filter the new list to only include scores greater than 100
# Say "keep x (for each x in new_scores) IF  x > 100"
scores_over_50 = [x for x in list1 if x < 50]

print('list1 values over 50:',scores_over_50)

# Map each element to its square
# Say "give me x squared (for each x in new_scores)"
triple_scores = [x * 3 for x in list1]

print('triple values:',triple_scores)

# list comprehension to transform your list into another list using a transformation

LIST = [item.upper() for item in list]

print('upper case list:',LIST)

print()
print("Add print statements to the code to see what happens.")
print("Explore enough to understand.")
print("Then apply what you know to your own domain.")
print()


# define some functions
def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

def yoga_techniques(list):
     for name in list:
        return list
print('Some of Yoga Techniques are :', list)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


print('area with couple of values from list1:', get_area_of_lot(list[3],list[5]))


