def lz78_encode(message):
    """
    Encodes the given message using the LZ78 compression algorithm.
    Displays only the final dictionary at the end.

    Parameters:
    - message (str): The input string to be encoded.

    Returns:
    - list of tuples: A list containing the encoded output pairs (index, character).
    """
    # Initialize the dictionary with the empty string at index 0
    dictionary = ['']
    output = []
    i = 0  # Current position in the message

    while i < len(message):
        current_string = ''
        index = 0
        # Find the longest prefix current_string in the dictionary
        while True:
            j = i + len(current_string)
            if j >= len(message):
                break
            c = message[j]
            candidate = current_string + c
            if candidate in dictionary:
                current_string = candidate
                index = dictionary.index(candidate)
                # Move to the next character
                continue
            else:
                # Add new entry to the dictionary
                dictionary.append(candidate)
                # Output the pair (index of current_string, next character c)
                output.append((index, c))
                # Move to the next part of the message
                i += len(current_string) + 1
                break
        else:
            # Handle the case when we reach the end of the message
            if current_string != '':
                index = dictionary.index(current_string)
                output.append((index, ''))
                i += len(current_string)
            break

    # Display final dictionary
    print("\nFinal Dictionary:")
    for idx, entry in enumerate(dictionary):
        print(f"  Index {idx}: '{entry}'")

    return output

def lz78_decode(encoded_pairs):
    """
    Decodes the given list of encoded pairs using the LZ78 decompression algorithm.

    Parameters:
    - encoded_pairs (list of tuples): The encoded output pairs (index, character).

    Returns:
    - str: The reconstructed original message.
    """
    # Initialize the dictionary with the empty string at index 0
    dictionary = ['']
    message = ''  # Reconstructed message

    # Process each encoded pair
    for idx, (index, c) in enumerate(encoded_pairs):
        if index < len(dictionary):
            s = dictionary[index]
            sc = s + c if c else s
            dictionary.append(sc)
            message += sc
        else:
            print(f"Error: Invalid index {index} at position {idx}")
            return ''
    # Display final dictionary
    print("\nFinal Dictionary:")
    for idx, entry in enumerate(dictionary):
        print(f"  Index {idx}: '{entry}'")

    return message

def parse_encoded_input(encoded_input):
    """
    Parses the encoded input string into a list of tuples.

    Parameters:
    - encoded_input (str): The input string containing encoded pairs.

    Returns:
    - list of tuples: Parsed list of encoded pairs (index, character).
    """
    import re
    # Regular expression to match pairs in the format (index, character)
    pattern = r'\((\d+),\s*(.*?)\)'
    matches = re.findall(pattern, encoded_input)
    encoded_pairs = []
    for idx, ch in matches:
        index = int(idx)
        # Handle 'EOF' or empty character
        if ch == 'EOF' or ch == '':
            c = ''
        else:
            # Remove quotes if present
            c = ch.strip('\'"')
        encoded_pairs.append((index, c))
    return encoded_pairs

# Main code to take user input and encode or decode the message
if __name__ == "__main__":
    # Prompt the user to choose encode or decode
    choice = input("Do you want to encode or decode a message? (Enter 'e' for encode or 'd' for decode): ").strip().lower()

    if choice == 'e':
        # Encoding mode
        # Prompt the user to enter the message
        message = input("Enter the message to encode using LZ78: ")

        # Encode the message
        encoded_output = lz78_encode(message)

        # Print the encoded output pairs
        print("\nEncoded Output:")
        for pair in encoded_output:
            if pair[1] == '':
                # Handle the case where the next character is empty (end of message)
                print(f"({pair[0]}, EOF)")
            else:
                print(f"({pair[0]}, '{pair[1]}')")

    elif choice == 'd':
        # Decoding mode
        # Prompt the user to enter the encoded pairs
        print("Enter the encoded pairs in the format (index, character), separated by commas.")
        print("Example: (0,a),(0,c),(1,b),(3,b),(4,a),(4,c)")
        encoded_input = input("Enter the encoded pairs: ")

        # Parse the encoded input into a list of tuples
        encoded_pairs = parse_encoded_input(encoded_input)

        # Decode the message
        message = lz78_decode(encoded_pairs)

        # Print the reconstructed message
        print("\nReconstructed Message:")
        print(message)
    else:
        print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")
