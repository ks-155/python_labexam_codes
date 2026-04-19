n=int(input("entre the number terms :"))
lst=[int(input("entre the num :"))for i in range(n)]
target=int(input("entre target sum:"))


def find_pairs(lst, target):
    seen = set()
    pairs = []
    
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

result = find_pairs(lst, target)
print("Pairs with target sum",  result)