age=int(input("entre the age :"))
def vote(age):
    if age>=18:
        return "yes"
    else:
        return "no"
    
result=vote(age)
print("here:",result)