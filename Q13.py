'''Write a Python program to find numbers in a list that have an even number of digits using a function.
•	Accept a list of integers from the user. 
•	Create a function that returns a list of numbers with even digits. 
•	Display the result.'''

def even_digit_numbers(lst):
    return [x for x in lst if len(str(abs(x))) % 2 == 0]

lst = list(map(int, input("Enter integers separated by space: ").split()))
print(even_digit_numbers(lst))

