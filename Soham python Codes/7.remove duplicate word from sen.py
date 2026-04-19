# sen=str(input("entre the sen :"))


# def removedupword(sentence):
#         words = sentence.split()
#         unique_words = []
#         for word in words:
#             if word not in unique_words:
#                 unique_words.append(word)
#         return ' '.join(unique_words)

# result= removedupword(sen)
# print("here :",result)

def remove_duplicates(sentence):
    unique_words = []
    for word in sentence.split():
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

sent = input("Enter a sentence: ")
print(remove_duplicates(sent))