n=int(input("enter number of elements :"))
lst=[int(n) for n in input("enter numbers :").split()]
def even(lst):
    return [x for x in lst if len(str(abs(x)))%2==0]

#result=even(lst)
print("even no of digits numbers :",even(lst))