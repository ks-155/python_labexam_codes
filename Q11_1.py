def even_nums(lst):
    result=0
    for i in lst:
        if i%2==0:
            result+=i
    return result
inputstr=[int(x) for x in input("Enter a list of numbers: ").split()]

print("Sum of even numbers in the list:", even_nums(inputstr))