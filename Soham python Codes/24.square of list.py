n=int(input("entre the terms for list:"))
lst=[]
for i in range(n):
    i=int(input("entre the elemnts :"))
    lst.append(i)
    
print("list is here :",lst)
def sqlist(list):
    return [x**2 for x in list]
result=sqlist(lst)
print("hereM:",result)