import itertools
from fractions import Fraction
import math

def generate_sequences(symbols, x):
    # Generate all sequences of length x
    sequences = list(itertools.product(symbols, repeat=x))
    seq_probs = []
    for seq in sequences:
        seq_symbols = ''.join([s[0] for s in seq])
        prob = Fraction(1, 1)
        for s in seq:
            prob *= s[1]
        seq_probs.append((seq_symbols, prob))
    return seq_probs

def shannon_fano(symbols_probs, r):
    # Assign codewords using Shannon-Fano algorithm with radix r
    def recursive_assign(symbols_probs, code_prefix):
        if len(symbols_probs) == 1:
            symbol = symbols_probs[0][0]
            codes[symbol] = code_prefix
            return
        total_prob = sum(prob for sym, prob in symbols_probs)
        cumulative_probs = [Fraction(0, 1)]
        for sym, prob in symbols_probs:
            cumulative_probs.append(cumulative_probs[-1] + prob)
        partitions = []
        idx = 0
        for i in range(1, r):
            target_prob = i * total_prob / r
            while idx < len(symbols_probs) and cumulative_probs[idx + 1] < target_prob:
                idx += 1
            partitions.append(symbols_probs[:idx + 1])
            symbols_probs = symbols_probs[idx + 1:]
            cumulative_probs = cumulative_probs[idx + 1:]
            idx = 0
        partitions.append(symbols_probs)
        for i, part in enumerate(partitions):
            recursive_assign(part, code_prefix + str(i))
    codes = {}
    symbols_probs.sort(key=lambda x: x[1], reverse=True)
    recursive_assign(symbols_probs, '')
    return codes

def compute_entropy(symbols):
    # Compute the entropy H(S) of the source symbols
    H = 0
    for symbol, prob in symbols:
        H -= float(prob) * math.log(float(prob), 2)
    return H

if __name__ == "__main__":
    symbols = [('a', Fraction(7, 11)), ('b', Fraction(3, 11)), ('c', Fraction(1, 11))]
    r = int(input("Enter the radix r: "))
    choice = input("Do you want to find 'codeword length' or 'probability'? Enter 'length' or 'probability': ").strip().lower()
    
    if choice == 'probability':
        x = int(input("Enter the extension order x: "))
        seq_probs = generate_sequences(symbols, x)
        seq_probs.sort(key=lambda x: x[1], reverse=True)
        codes = shannon_fano(seq_probs, r)
        for seq, code in codes.items():
            # Display the probability alongside the codeword in fraction form
            prob = next(prob for s, prob in seq_probs if s == seq)
            print(f"{seq}: {code}, Probability: {prob}")
    elif choice == 'length':
        # Compute the entropy H(S)
        H_S = compute_entropy(symbols)
        # Compute the average codeword length per symbol as H(S) / log2(r)
        average_length_per_symbol = H_S / math.log2(r)
        print(f"\nEntropy H(S): {H_S:.3f}")
        print(f"As n -> ∞, the average codeword length per symbol of the radix {r} Huffman code for S^n converges to: {average_length_per_symbol:.3f}")
    else:
        print("Invalid choice. Please enter 'length' or 'probability'.")