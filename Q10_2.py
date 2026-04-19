n1=int(input("enter number of elements for list 1: "))
lst1=[int(x) for x in input("Enter elements seperated by space: ").split() for i in range(n1)]
n2=int(input("enter number of elements for list 2: "))
lst2=[int(x) for x in input("Enter elements seperated by space: ").split() for i in range(n2)]

def intersection(lst1,lst2):
    return(set(lst1) & set(lst2))
result=list(intersection(lst1,lst2))
print("common elements are: ",result)































































