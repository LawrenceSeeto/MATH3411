# Combined Program: Kraft-McMillan Solver and Canonical Prefix Code Assignment

import math
from typing import List

def kraft_mcmillan_solver():
    print("\nKraft-McMillan Solver for Unknown Codeword Lengths")
    try:
        r = int(input("Enter the radix (size of the coding alphabet): "))
        known_lengths_input = input("Enter the known codeword lengths, separated by spaces: ")
        known_lengths = list(map(int, known_lengths_input.strip().split()))
        total_K_input = input("Enter the total Kraft-McMillan coefficient K (e.g., 61/64): ")
        # Evaluate total_K if it's a fraction
        total_K = eval(total_K_input)
    
        # Calculate the sum of the contributions of known codeword lengths
        K_known = sum((1 / r) ** l for l in known_lengths)
        
        # Remaining contribution for unknown codewords
        K_remaining = total_K - K_known
        
        if K_remaining <= 0:
            print("No remaining code space. Check your inputs.")
            return
        elif K_remaining > 1:
            print("Total K cannot exceed 1. Check your inputs.")
            return
        
        # Calculate the minimal integer length for the unknown codeword
        l_n = math.log(1 / K_remaining, r)
        l_n_int = math.ceil(l_n)
    
        print(f"The value of the unknown codeword length is: {l_n_int}")
    
    except ValueError:
        print("Invalid input. Please enter integer values for lengths and a valid K.")
    except ZeroDivisionError:
        print("Radix r cannot be zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def assign_codewords(lengths):
    """
    Assign codewords to symbols using the canonical prefix code method.

    Parameters:
    - lengths: A list of tuples where each tuple contains (symbol_index, codeword_length)

    Returns:
    - codewords: A dictionary mapping symbol indices to their assigned codewords
    """
    # Step 1: Sort the symbols based on their codeword lengths
    sorted_lengths = sorted(lengths, key=lambda x: x[1])

    codewords = {}
    C = 0  # Codeword counter
    l_prev = 0  # Previous codeword length

    # Step 2: Assign codewords to each symbol
    for symbol_index, l_i in sorted_lengths:
        if l_i > l_prev:
            # Shift C left by the difference in lengths
            C = C << (l_i - l_prev)
        # Format the codeword with leading zeros to match the codeword length
        codeword = format(C, '0{}b'.format(l_i))
        codewords[symbol_index] = codeword
        # Increment the codeword counter
        C += 1
        # Update the previous length
        l_prev = l_i

    return codewords

def canonical_prefix_code_assignment():
    print("\nCanonical Prefix Code Assignment")
    try:
        # Step 1: Get codeword lengths from the user
        num_symbols = int(input("Enter the number of symbols: "))
        print("Enter the codeword lengths for each symbol, separated by spaces:")
        lengths_input = input().strip()

        # Convert the input string to a list of integers
        lengths_list = list(map(int, lengths_input.split()))
        if len(lengths_list) != num_symbols:
            print("The number of codeword lengths provided does not match the number of symbols.")
            return

        # Create a list of tuples (symbol_index, codeword_length)
        # Symbols are indexed starting from 1 (s1, s2, ...)
        lengths = [(i + 1, l_i) for i, l_i in enumerate(lengths_list)]

        # Step 2: Get the symbol index for which to find the codeword
        symbol_index = int(input(f"Enter the symbol index (1 to {num_symbols}) to find its codeword: "))
        if symbol_index < 1 or symbol_index > num_symbols:
            print(f"Symbol index must be between 1 and {num_symbols}.")
            return

        # Step 3: Assign codewords to the symbols
        codewords = assign_codewords(lengths)

        # Step 4: Output the codeword for the specified symbol
        print(f"The codeword corresponding to symbol s{symbol_index} is: {codewords[symbol_index]}")

        # Optional: Output all codewords
        print("\nAll assigned codewords:")
        for idx in range(1, num_symbols + 1):
            print(f"Symbol s{idx}: {codewords[idx]}")

    except ValueError:
        print("Invalid input. Please enter integer values.")

def main():
    print("Choose an option:")
    print("1. Kraft-McMillan Solver for Unknown Codeword Lengths")
    print("2. Canonical Prefix Code Assignment")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        kraft_mcmillan_solver()
    elif choice == '2':
        canonical_prefix_code_assignment()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
