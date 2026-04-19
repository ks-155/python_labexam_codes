n=int(input("entre the numbers fro elemnts :"))
lst=[int(input("entre the numbers :")) for i in range(n)]

def isprime(n,count=0):
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

def findp(lst):
    return list(filter(isprime,lst))

result=findp(lst)
print("here :",result)