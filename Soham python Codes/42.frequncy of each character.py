text=input("Enter the string:")

def frch(str):
    
    chardic={}
    for char in text:
        chardic[char]=text.count(char)
    return chardic
    
result=frch(text)
print("here :",result)