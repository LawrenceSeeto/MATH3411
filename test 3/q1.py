import math
from fractions import Fraction

def shannon_fano_coding(probabilities, radix):
    """
    Perform Shannon-Fano coding for given probabilities and radix.

    Parameters:
    - probabilities: List of symbol probabilities (should sum to 1).
    - radix: The base of the code (e.g., 2 for binary, 3 for ternary).

    Returns:
    - A tuple containing:
        - codewords: List of codewords represented as strings in the given radix.
        - codeword_lengths: List of codeword lengths.
    """
    # Step 1: Compute codeword lengths
    codeword_lengths = []
    for p in probabilities:
        l = math.ceil(-math.log(p, radix))
        codeword_lengths.append(l)
    
    # Step 2: Construct the standard I-code
    codewords = []
    # Initialize codeword value
    code_value = 0
    for idx, length in enumerate(codeword_lengths):
        # Convert code_value to radix representation with specified length
        codeword = number_in_base(code_value, radix, length)
        codewords.append(codeword)
        # Increment code_value for next codeword
        code_value += 1
        # Multiply code_value by radix^(length difference) if next codeword length increases
        if idx + 1 < len(codeword_lengths):
            lengths_diff = codeword_lengths[idx + 1] - codeword_lengths[idx]
            code_value *= radix ** lengths_diff
    
    return codewords, codeword_lengths

def number_in_base(n, base, length):
    """
    Convert an integer to a string representation in a given base with fixed length.

    Parameters:
    - n: The integer number to convert.
    - base: The base for conversion.
    - length: The fixed length of the output string.

    Returns:
    - A string representing the number in the given base with leading zeros if necessary.
    """
    if n == 0:
        return '0' * length
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    # Pad with zeros to match the desired length
    while len(digits) < length:
        digits.append('0')
    return ''.join(reversed(digits))

# Example usage:
if __name__ == "__main__":
    # Input: List of probabilities and radix
    probabilities = [0.5, 0.3, 0.1, 0.1]
    radix = 3  # Binary code

    # Perform Shannon-Fano coding
    codewords, codeword_lengths = shannon_fano_coding(probabilities, radix)

    # Output the results
    symbols = ['A', 'B', 'C', 'D']
    print("Symbol\tProbability\tCodeword\tLength")
    for symbol, p, codeword, length in zip(symbols, probabilities, codewords, codeword_lengths):
        print(f"{symbol}\t{p}\t\t{codeword}\t\t{length}")

    # Compute the average codeword length in fraction form
    average_length = sum(Fraction(p).limit_denominator() * length for p, length in zip(probabilities, codeword_lengths))
    print(f"\nAverage codeword length: {average_length}")

    # Encode the message m = s1 s4 s2 s1
    message = ['C', 'C', 'C', 'A']
    symbol_to_codeword = dict(zip(symbols, codewords))
    encoded_message = ''.join([symbol_to_codeword[symbol] for symbol in message])
    print(f"\nEncoded message: {encoded_message}")
