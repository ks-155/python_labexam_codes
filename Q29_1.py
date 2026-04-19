def remove_vowels(s):
    result = ""
    for char in s:
        if char.lower() in 'aeiou':
            result += char
    return result

text = input("Enter a string: ")
print(len(remove_vowels(text)))