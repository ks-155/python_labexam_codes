def remove_vowels(s):
    result= ""

    for char in s:
        if char.lower() not in 'aeiou':
            result=result+char
    return result
    
input_string=input("Enter a string: ")
print("vowels removed string:",remove_vowels(input_string))

    