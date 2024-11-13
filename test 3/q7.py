from math import gcd
from sympy import totient as phi

def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

def find_primitive_elements_Zp(p, exclude=None):
    primitive_elements = [g for g in range(1, p) if is_primitive_root(g, p)]
    if exclude is not None and exclude in primitive_elements:
        primitive_elements.remove(exclude)
    return primitive_elements

def count_primitive_elements_GF(x):
    phi_value = phi(x - 1)
    return phi_value

def count_primitive_elements_Zp(p):
    phi_p = phi(p)
    phi_phi_p = phi(phi_p)
    return phi_phi_p

def main():
    print("Which question are you trying to solve?")
    print("1. Find all primitive elements of Z_p")
    print("2. How many primitive elements does the field GF(x) have?")
    print("3. How many primitive elements does the group of units in Z_p have?")
    
    choice = int(input("Enter 1, 2, or 3: "))
    
    if choice == 1:
        p = int(input("Enter the value of p: "))
        exclude = int(input("Enter the primitive element to exclude: "))
        primitive_elements = find_primitive_elements_Zp(p, exclude)
        print(f"Primitive elements of Z_{p} excluding {exclude}: {primitive_elements}")
    elif choice == 2:
        x = int(input("Enter the value of x: "))
        num_primitive_elements = count_primitive_elements_GF(x)
        print(f"Number of primitive elements in GF({x}): {num_primitive_elements}")
    elif choice == 3:
        p = int(input("Enter the value of p: "))
        num_primitive_elements = count_primitive_elements_Zp(p)
        print(f"Number of primitive elements in the group of units in Z_{p}: {num_primitive_elements}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()