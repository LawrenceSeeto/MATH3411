# Arithmetic Coding Encoder

def get_cumulative_probabilities(symbols, probabilities):
    cumulative_probs = {}
    cumulative = 0.0
    for symbol, prob in zip(symbols, probabilities):
        cumulative_probs[symbol] = (cumulative, cumulative + prob)
        cumulative += prob
    return cumulative_probs

def arithmetic_encode(message, cumulative_probs):
    lower_bound = 0.0
    upper_bound = 1.0

    for symbol in message:
        symbol_low, symbol_high = cumulative_probs[symbol]
        range_ = upper_bound - lower_bound
        upper_bound = lower_bound + range_ * symbol_high
        lower_bound = lower_bound + range_ * symbol_low

    # Return any number within the final interval
    encoded_value = (lower_bound + upper_bound) / 2
    return encoded_value

def main():
    # Input symbols and probabilities
    num_symbols = int(input("Enter the number of symbols: "))
    symbols = []
    probabilities = []

    print("\nEnter the symbols and their probabilities:")
    for _ in range(num_symbols):
        symbol = input("Symbol: ")
        prob = float(input(f"Probability of '{symbol}': "))
        symbols.append(symbol)
        probabilities.append(prob)

    # Check if probabilities sum to 1
    if abs(sum(probabilities) - 1.0) > 1e-6:
        print("\nError: Probabilities must sum up to 1.")
        return

    # Get the message to encode
    message = input("\nEnter the message to encode: ")

    # Build cumulative probabilities
    cumulative_probs = get_cumulative_probabilities(symbols, probabilities)

    # Encode the message
    encoded_value = arithmetic_encode(message, cumulative_probs)

    print(f"\nEncoded value for the message '{message}': {encoded_value}")

    # Optionally, display the cumulative probabilities
    print("\nCumulative Probabilities:")
    for symbol in symbols:
        low, high = cumulative_probs[symbol]
        print(f"Symbol '{symbol}': Interval [{low}, {high})")

if __name__ == "__main__":
    main()
