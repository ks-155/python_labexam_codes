n=int(input("Enter the number of elements: "))
lst=[int(input("entre the numbers :")) for i in range(n)]
def isprime(n,count=0):
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            
    if count==2:
        return True
    else:
        return False
            
def removeprime(lst):
    return list(filter(lambda x:not isprime(x),lst))
result=removeprime(lst)
print("removed prime numbers: ",result)