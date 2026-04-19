name=str(input("entre the name :"))

def res(str):
    a = str.count('a') + str.count('A')
    e = str.count('e') + str.count('E')
    i = str.count('i') + str.count('I')
    o = str.count('o') + str.count('O')
    u = str.count('u') + str.count('U')
    vovel=a+e+i+o+u
    const=len(str)-vovel
    return vovel,const

vovel,constant=res(name)
print("v is here :",vovel)
print("c is here :",constant)