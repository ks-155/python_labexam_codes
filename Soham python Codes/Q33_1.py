
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

def sum_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return sum,avg

sum,avg=sum_avg(a,b,c)
print("The sum is:",sum)
print("The average is:",avg)


