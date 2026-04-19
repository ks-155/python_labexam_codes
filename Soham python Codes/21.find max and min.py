lst=[1,2,3,67,89,54,0,56,44,99]
def mm(lst):
    maximum=lst[0]
    minimum=lst[0]
    for x in lst:
        if x>maximum:
            maximum=x
        elif x<minimum:
            minimum=x
    return maximum,minimum
maximum,minimum=mm(lst)
print("max :",maximum)
print("min:",minimum)
