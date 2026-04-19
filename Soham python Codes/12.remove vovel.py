name=str(input("enter the string :"))
def rev(str):
    return "".join(ch for ch in str if ch.lower() not in "aeiou")
result=rev(name)
print("vowels removed :",result)


