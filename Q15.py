'''Write a Python program to print the Fibonacci series up to the nth term using a recursive function.
•	The program should: 
o	Accept a positive integer n from the user. 
o	Use a recursive function to generate Fibonacci numbers. 
o	Display the Fibonacci series up to n terms. 
Note:
•	The Fibonacci series is defined as: 
o	F(0) = 0 
o	F(1) = 1 
o	F(n) = F(n−1) + F(n−2), for n ≥ 2 
'''

def recfibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return recfibo(n-1) + recfibo(n-2)

n = int(input("Enter n: "))
for i in range(n):
    print(recfibo(i), end=" ")