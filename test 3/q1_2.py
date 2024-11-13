import math

def compute_codeword_length(p, radix):
    """
    Compute the codeword length for a symbol in a Shannon-Fano code.

    Parameters:
    - p: Probability of the symbol.
    - radix: Radix of the code (e.g., 2 for binary, 3 for ternary).

    Returns:
    - The codeword length as an integer.
    """
    # Calculate the codeword length
    l = math.ceil(-math.log(p, radix))
    return l

# Example usage:
if __name__ == "__main__":
    # Given probability
    p_s = 0.42
    # Radix for ternary code
    radix = 3

    # Compute the codeword length
    codeword_length = compute_codeword_length(p_s, radix)

    # Output the result
    print(f"The length of the codeword is: {codeword_length}")
