
'''Write a Python program to find all pairs of numbers in a list whose sum equals a given number using a function.
•	Accept a list of integers and a target sum from the user. 
•	Create a function that returns a list of tuples, each representing a pair. 
•	Display the result.

'''
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

lst = list(map(int, input("Enter integers separated by space: ").split()))
target = int(input("Enter target sum: "))
print(find_pairs(lst, target))