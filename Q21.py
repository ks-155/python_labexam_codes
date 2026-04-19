'''21.	Write a Python program to find the maximum and minimum values in a list using a function.
•	Create a list of numbers. 
•	Create a function that takes the list as input. 
•	Find maximum and minimum inside the function. 
•	Return both values from the function. 
•	Display the results.'''

import math
random_nums=[5,1,10,25]
def max_nums():
    print("max num: ",max(random_nums))
def min_nums():
    print("min num: ",min(random_nums))

min_nums()
max_nums()