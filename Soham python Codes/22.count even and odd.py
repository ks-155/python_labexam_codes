lst=[1,12,23,34,44,45,56,67,78,89,77,66,33,21]
def oec(lst,count=0):
    for i in lst:
        if i%2==0:
            count+=1
    return {"even":count,"odd":len(lst)-count}

result=oec(lst)
print("result is here :",result)