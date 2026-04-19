n=int(input("entre the terms for list:"))
lst=[]
for i in range(n):
    i=int(input("entre the elemnts :"))
    lst.append(i)
    
print("list is here :",lst)

def lstsort(list):
    return sorted(list)

result=lstsort(lst)
print("here :",result)