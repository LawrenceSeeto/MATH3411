from collections import defaultdict

def generate_strings(codewords, max_length):
    """
    Generate all possible strings by concatenating codewords up to a certain length.
    """
    results = set()
    current_strings = ['']
    while current_strings:
        next_strings = []
        for s in current_strings:
            for cw in codewords:
                new_s = s + cw
                if len(new_s) <= max_length:
                    results.add(new_s)
                    next_strings.append(new_s)
        current_strings = next_strings
    return results

def count_parsings(s, codeword_set, memo=None):
    """
    Count the number of ways to parse the string s into codewords from the set.
    Uses dynamic programming to store intermediate results.
    """
    if memo is None:
        memo = {}
    if s in memo:
        return memo[s]
    if not s:
        return 1  # Empty string can be parsed in one way

    count = 0
    for cw in codeword_set:
        if s.startswith(cw):
            remainder = s[len(cw):]
            count += count_parsings(remainder, codeword_set, memo)
    memo[s] = count
    return count

def main():
    # Get initial codewords from user
    n = int(input("Enter the number of initial codewords: "))
    codewords = []
    for i in range(n):
        cw = input(f"Enter codeword c{i+1}: ")
        codewords.append(cw)

    # Get options from user
    num_options = int(input("Enter the number of options for c4: "))
    options = []
    for i in range(num_options):
        c4 = input(f"Enter codeword for option {i+1} (type 'None' if no codeword): ")
        c4 = c4 if c4.lower() != 'none' else None
        options.append(c4)

    max_codeword_length = max(len(cw) for cw in codewords + [c for c in options if c])
    max_length = max_codeword_length * 4  # Adjust as needed

    # Generate all possible concatenations of initial codewords
    initial_strings = generate_strings(codewords, max_length)

    # Check each option
    for idx, c4 in enumerate(options, start=1):
        if c4 is None or c4 == '':
            print(f"\nOption {idx}: None (No c4 provided)")
            codeword_set = set(codewords)
        else:
            print(f"\nOption {idx}: c4 = '{c4}'")
            codeword_set = set(codewords + [c4])

        # Generate new strings by inserting c4 into every possible position
        ambiguous = False
        for s in initial_strings:
            for i in range(len(s) + 1):
                new_s = s[:i] + c4 + s[i:] if c4 else s
                if len(new_s) > max_length:
                    continue
                # Count the number of ways to parse new_s
                num_parsings = count_parsings(new_s, codeword_set)
                if num_parsings > 1:
                    print(f"Ambiguity found in string '{new_s}' which can be parsed in {num_parsings} ways.")
                    ambiguous = True
                    break  # Stop at the first ambiguity found
            if ambiguous:
                break
        result = "Not Uniquely Decodable" if ambiguous else "Uniquely Decodable"
        print(f"Result: The code is {result}")

if __name__ == "__main__":
    main()

