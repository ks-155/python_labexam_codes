n=int(input("enter number of elements :"))
lst=[int(n) for n in input("enter  elements :").split()]

def isprime(n,count=0):
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

def remove_primes(lst):
    return list(filter(lambda x:not isprime(x),lst))

result=remove_primes(lst)
print("numbers after removing primes :",result)