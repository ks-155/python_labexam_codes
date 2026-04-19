
n = int(input("Enter the number of elements: "))
lst = [int(input("Enter the number: ")) for i in range(n)]


def fr(lst):
    freq_dict = {}
    for element in lst:
        freq_dict[element] = lst.count(element)
    return freq_dict

result = fr(lst)
print("Frequency:", result)