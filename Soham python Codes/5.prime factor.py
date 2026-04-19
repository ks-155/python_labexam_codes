
num = int(input("Enter number: "))

def prime_factors(n):
    
    if n == 1:
        return []
    
    
    for i in range(2, n + 1):
        if n % i == 0:
            return [i] + prime_factors(n // i)


print(f"Prime factors: {prime_factors(num)}")