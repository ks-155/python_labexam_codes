sen = str(input("Enter the sentence: "))

def rword(s):
    words = s.split()
    reversewords = [word[::-1] for word in words]  
    return " ".join(reversewords)  

result = rword(sen)
print("here b:", result)

