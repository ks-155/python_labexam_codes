n=int(input("entre the number :"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
factorial=fact(n)
print("factorial is here:",factorial)