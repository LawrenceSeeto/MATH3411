def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(x, n):
    gcd, inv, _ = extended_gcd(x, n)
    if gcd != 1:
        return 0  # No inverse exists if gcd is not 1
    else:
        return inv % n

def order_mod_n(a, n):
    if gcd(a, n) != 1:
        return 0  # No order if a and n are not coprime
    k = 1
    power = a % n
    while power != 1:
        power = (power * a) % n
        k += 1
    return k

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def main():
    mode = input("Enter mode (inverse, order, units): ").strip().lower()
    if mode == "inverse":
        x = int(input("Enter the number x: "))
        n = int(input("Enter the modulus n: "))
        inverse = mod_inverse(x, n)
        if inverse == 0:
            print(f"No inverse exists for {x} in Z_{n}")
        else:
            print(f"The inverse of {x} in Z_{n} is {inverse}")
    elif mode == "order":
        a = int(input("Enter the number a: "))
        n = int(input("Enter the modulus n: "))
        order = order_mod_n(a, n)
        if order == 0:
            print(f"No order exists for {a} in Z_{n}")
        else:
            print(f"The order of {a} in Z_{n} is {order}")
    elif mode == "units":
        n = int(input("Enter the modulus n: "))
        units = euler_totient(n)
        print(f"The number of units in Z_{n} is {units}")

if __name__ == "__main__":
    main()