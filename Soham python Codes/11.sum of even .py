n1=int(input("entree the numbers of elemnts of list1 :"))
lst1=[int(input("entter the elments :")) for i in range(n1)]

def evensum(list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i
    return sum

result=evensum(lst1)
print("here",result)