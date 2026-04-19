n1=int(input("entree the numbers of elemnts of list1 :"))
lst1=[int(input("entter the elments :")) for i in range(n1)]
k=int(input("enter the number k:"))

def divk(list,k):
    return [i for i in list if i%k==0]
        
result=divk(lst1,k)
print("here :",result)