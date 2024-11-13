import math

def fermat_factorization(n):
    x = math.ceil(math.sqrt(n))
    while True:
        y2 = x * x - n
        y = int(math.sqrt(y2))
        if y * y == y2:
            a = x - y
            b = x + y
            if a >= 2 and a < b:
                return b - a
        x += 1

# Example usage
n = 81719
result = fermat_factorization(n)
print(f"The value of b - a for n = {n} is {result}")