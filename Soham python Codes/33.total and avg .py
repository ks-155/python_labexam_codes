m1=int(input("entre the marks 1:"))
m2=int(input("entre the marks 2:"))
m3=int(input("entre the marks 3:"))

def res(m1,m2,m3):
    total=m1+m2+m3
    avg=total/3.0
    return total,avg

total,avg=res(m1,m2,m3)
print("t is here:",total)
print("...:",avg)