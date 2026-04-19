n=int(input("entre the numbers fro elemnts :"))
lst=[int(input("entre the numbers :")) for i in range(n)]

def pal(n):
    s=str(n)
    return s==s[::-1]
       
    
def ispal(lst):
    return[x for x in lst if pal(x)]

result=ispal(lst)
print("here :",result)