lst=[1,2,3,3,4,5,6,4,3,2,1,5,55,5,5,5,5,5,6,7]
def removed(l):
    return list(set(l))

result=removed(lst)
print("here :",result)