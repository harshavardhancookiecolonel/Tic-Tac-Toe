# Read a string of 9 symbols from the input
input_string = input("Enter a string of 9 symbols (X, O, _): ")

# Check if the input length is exactly 9 characters
if len(input_string) != 9:
    print("Input string must have exactly 9 characters.")
else:
    # Output the grid with formatting
    print("---------")
    for i in range(0, 9, 3):
        row = input_string[i:i+3]
        print("|", " ".join(row), "|")
    print("---------")
