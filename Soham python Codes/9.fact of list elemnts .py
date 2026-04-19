from functools import reduce
n=int(input("entre the numbers fro elemnts :"))
lst=[int(input("entre the numbers :")) for i in range(n)]

def factorial(n):
    if n < 2:
        return 1
    return reduce(lambda a, b: a * b, range(1, n + 1))


result = list(map(factorial, lst))

print("Factorials:", result)


""""""""""""""""
import math

lst = [1, 2, 3, 4, 5, 6]

# Using built-in math.factorial
result = list(map(math.factorial, lst))
print("Original:", lst)
print("Factorials:", result)

"""""""""""""""""