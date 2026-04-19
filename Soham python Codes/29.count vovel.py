name=str(input("ENTER THE NAME"))
print("This is your string : ",name)

def vovel(str):
    
   a = str.count('a')
   e = str.count('e')
   i = str.count('i')
   o = str.count('o')
   u = str.count('u')

   return a+e+i+o+u

result=vovel(name)
print("Total vovel is here : ",result)