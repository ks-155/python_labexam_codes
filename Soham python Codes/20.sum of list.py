n=int(input("entre the terms for list:"))
lst=[]
for i in range(n):
    i=int(input("entre the elemnts :"))
    lst.append(i)
    
print("list is here :",lst)

def sumlist(list):
    sum=0
    for elemnet in list:
        sum+=elemnet
        
    return sum

result=sumlist(lst)
print("here :",result)