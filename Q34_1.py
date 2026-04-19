'''names=['Prashant','Krish','Vijayalakshmi']
new_lst=list(filter(lambda x:len(x)>5,names))
print("updated list: ",new_lst)'''


from functools import reduce

n=int(input("enter the numbers from elements: "))
lst=[int(input("enter the numbers: "))for i in range(n)]
maximum=reduce(lambda a,b: a if a>b else b,lst)
print("result is here:",maximum)
