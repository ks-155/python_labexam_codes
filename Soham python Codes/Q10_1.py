n1=int(input("Enter number of elements in list1: "))
list1=[int(x) for x in input("Enter elements: ").split() for i in range(n1)]

n2=int(input("Enter number of elements in list2: "))
list2=[int(x) for x in input("Enter elements: ").split() for i in range(n2)]    

def intersection(list1, list2):
    return list(set(list1) & list(set(list2)))
result = intersection(list1, list2)
print("Intersection of the two lists is: ", result)