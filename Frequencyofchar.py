

# text=input("Enter the string:")
text=input("Enter the string:")
#words=text.split()
#strdic={}
def freq_char(char):
        strdic={}

        for char in text:
         strdic[char]=text.count(char)
        return strdic
    

result=freq_char(text)   
print("Our Result Is Here:",result)