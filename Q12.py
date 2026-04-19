'''Write a Python program to remove all vowels from a string using a function.
•	Accept a string from the user. 
•	Create a function that returns the string after removing vowels. 
•	Display the result.'''

#CODE:
def remove_vowels(s):
    result = ""
    for char in s:
        if char.lower() not in 'aeiou':
            result += char
    return result

text = input("Enter a string: ")
print(remove_vowels(text))