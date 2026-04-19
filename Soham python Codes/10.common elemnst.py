n1=int(input("entree the numbers of elemnts of list1 :"))
lst1=[int(input("entter the elments :")) for i in range(n1)]
n2=int(input("entree the numbers of elemnts of list2 :"))
lst2=[int(input("entter the elments :")) for i in range(n2)]


def common(lst1,lst2):
    return list(set(lst1) & set(lst2))
result=common(lst1,lst2)
print("here:",result)