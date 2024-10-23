def comma_code(x):
    # Generate a list of items based on the length x
    items = [f"item{i}" for i in range(1, x + 1)]

    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        # Join all items except the last with commas, then add ', and ' before the last item
        return ', '.join(items[:-1]) + ', and ' + items[-1]

# Get the length x from the user
x = int(input("Enter the length x: "))

# Generate and print the comma code
result = comma_code(x)
print(result)
