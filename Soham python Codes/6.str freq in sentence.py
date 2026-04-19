text=input("Enter the string:")

def fr(str):
    words=text.split()
    strdic={}
    for word in words:
        strdic[word]=words.count(word)
    return strdic
result=fr(text)
print("gere :",result)
    