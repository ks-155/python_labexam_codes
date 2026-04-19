lst = [10, 20, 4, 45, 99, 99, 67]

def second_largest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort(reverse=True)           
    return unique_lst[1]        
result = second_largest(lst)
print("Second largest:", result)  