'''Write a Python program to calculate the factorial of a given number using a recursive function.
•	The program should: 
o	Accept a non-negative integer n from the user. 
o	Use a recursive function to compute the factorial. 
o	Display the factorial of the given number. 
Note:
•	The factorial of a number is defined as: 
o	n! = 1, if n = 0 or n = 1 
o	n! = n × (n−1)!, for n > 1
'''
def recfact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recfact(n - 1)

n = int(input("Enter a non-negative integer: "))
print(recfact(n)) 