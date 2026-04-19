n=int(input("entre the number :"))
def prime(n,count=0):
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("yes")
    else:
        print("not ")
        
        
prime(n)