def is_strong_pseudo_prime(N, a):
    # Write (N-1) as 2^s * d
    s = 0
    d = N - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Compute a^d % N
    x = pow(a, d, N)
    if x == 1 or x == N - 1:
        return True

    # Repeat s-1 times: compute x^2 % N
    for _ in range(s - 1):
        x = pow(x, 2, N)
        if x == N - 1:
            return True

    return False

def is_pseudo_prime(N, a):
    return pow(a, N-1, N) == 1

def check_pseudo_primes(N, bases, check_type):
    if check_type == 1:
        return {a: is_strong_pseudo_prime(N, a) for a in bases}
    elif check_type == 2:
        return {a: is_pseudo_prime(N, a) for a in bases}
    else:
        raise ValueError("Invalid check type")

# Main program
if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    bases = list(map(int, input("Enter the bases separated by spaces: ").split()))
    print("What are you trying to find?")
    print("1. Strong pseudo-prime")
    print("2. Pseudo-prime")
    check_type = int(input("Enter 1 or 2: "))

    results = check_pseudo_primes(N, bases, check_type)
    true_bases = [a for a, is_pseudo_prime in results.items() if is_pseudo_prime]

    if true_bases:
        print(f"Bases for which N={N} is a {'strong pseudo-prime' if check_type == 1 else 'pseudo-prime'}: {true_bases}")
    else:
        print("None Of These")