import itertools
import math
from fractions import Fraction

def get_user_input():
    # Get the number of symbols and their probabilities
    num_symbols = int(input("Enter the number of symbols in the source: "))
    probabilities = []
    for i in range(num_symbols):
        prob_input = input(f"Enter probability of symbol {i+1} (as fraction, e.g., '6/7'): ")
        prob = float(Fraction(prob_input))
        probabilities.append(prob)
    symbols = [f's{i+1}' for i in range(num_symbols)]
    
    # Normalize probabilities if they don't sum to 1
    total_prob = sum(probabilities)
    if total_prob != 1:
        probabilities = [p / total_prob for p in probabilities]
        print("Probabilities normalized since they did not sum to 1.")
    
    radix = int(input("Enter the radix for Huffman coding (e.g., 3): "))
    extension_level = int(input("Enter the extension level (e.g., 3): "))
    
    return symbols, probabilities, radix, extension_level

def generate_extension(symbols, probabilities, n):
    # Generate all possible sequences of length n and their probabilities
    sequences = list(itertools.product(symbols, repeat=n))
    seq_probs = []
    seq_symbols = []
    prob_dict = dict(zip(symbols, probabilities))
    for seq in sequences:
        seq_symbol = ''.join(seq)
        seq_prob = 1
        for s in seq:
            seq_prob *= prob_dict[s]
        seq_symbols.append(seq_symbol)
        seq_probs.append(seq_prob)
    return seq_symbols, seq_probs

def add_dummy_symbols(seq_symbols, seq_probs, radix):
    # Add dummy symbols to make the total number of symbols a multiple of the radix
    num_symbols = len(seq_symbols)
    remainder = num_symbols % radix
    if remainder != 0:
        num_dummy = radix - remainder
        for i in range(num_dummy):
            dummy_symbol = f"DUMMY_{i+1}"
            seq_symbols.append(dummy_symbol)
            seq_probs.append(0)
    return seq_symbols, seq_probs

def build_huffman_tree(seq_symbols, seq_probs, radix):
    # Build the Huffman tree using radix-n
    import heapq
    heap = [ (prob, [symbol]) for symbol, prob in zip(seq_symbols, seq_probs) ]
    heapq.heapify(heap)
    
    code_dict = {}
    while len(heap) > 1:
        # Take 'radix' number of nodes with smallest probabilities
        nodes = [ heapq.heappop(heap) for _ in range(min(radix, len(heap))) ]
        combined_prob = sum(node[0] for node in nodes)
        combined_symbols = []
        for idx, node in enumerate(nodes):
            for symbol in node[1]:
                combined_symbols.append(symbol)
                if symbol not in code_dict:
                    code_dict[symbol] = ''
                code_dict[symbol] = str(idx) + code_dict[symbol]
        # Push the combined node back into the heap
        heapq.heappush(heap, (combined_prob, combined_symbols))
    return code_dict

def calculate_average_length(code_dict, seq_symbols, seq_probs):
    # Calculate the average codeword length
    total_length = 0
    total_prob = sum(seq_probs)
    for symbol in seq_symbols:
        if "DUMMY" not in symbol:
            idx = seq_symbols.index(symbol)
            prob = seq_probs[idx]
            total_length += prob * len(code_dict[symbol])
    return total_length / total_prob

# Main program
if __name__ == "__main__":
    # Step 1: Get user input
    symbols, probabilities, radix, extension_level = get_user_input()
    
    # Step 2: Generate the extension
    seq_symbols, seq_probs = generate_extension(symbols, probabilities, extension_level)
    
    # Step 3: Sort the sequences in decreasing order of probabilities
    combined = list(zip(seq_symbols, seq_probs))
    combined.sort(key=lambda x: x[1], reverse=True)
    seq_symbols, seq_probs = zip(*combined)
    seq_symbols = list(seq_symbols)
    seq_probs = list(seq_probs)
    
    # Step 4: Add dummy symbols if necessary
    seq_symbols, seq_probs = add_dummy_symbols(seq_symbols, seq_probs, radix)
    
    # Step 5: Build the Huffman tree
    code_dict = build_huffman_tree(seq_symbols, seq_probs, radix)
    
    # Step 6: Calculate the average codeword length
    avg_length = calculate_average_length(code_dict, seq_symbols, seq_probs)
    
    # Step 7: Output the results
    print("\nHuffman Codes:")
    for symbol in seq_symbols:
        if "DUMMY" not in symbol:
            print(f"Symbol: {symbol}, Codeword: {code_dict[symbol]}")
    print(f"\nAverage codeword length: {avg_length}")
