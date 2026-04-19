n = int(input("Enter which Fibonacci number to find: "))
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for x in range(1,n):
    print(fibonacci(x))