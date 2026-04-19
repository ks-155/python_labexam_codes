#11 sum of even numbers
def sum_of_evens(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

lst = list(map(int, input("Enter integers separated by space: ").split()))
print(sum_of_evens(lst))




