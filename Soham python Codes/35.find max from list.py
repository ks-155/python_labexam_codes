from functools import reduce


n=int(input("entre the numbers from elements :"))
lst=[int(input("enter the numbers (press enter after each num):")) for i in range(n)]
maximum=reduce(lambda a,b: a if a>b else b,lst)
print("maximum is :",maximum)


