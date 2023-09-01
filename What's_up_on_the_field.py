# Read a string of 9 symbols from the input
input_string = input("Enter a string of 9 symbols (X, O, _): ")

# Check if the input length is exactly 9 characters
if len(input_string) != 9:
    print("Input string must have exactly 9 characters.")
else:
    # Output the grid with formatting
    print("---------")
    for i in range(0, 9, 3):
        row = input_string[i:i + 3]
        print("|", " ".join(row), "|")
    print("---------")

    # Function to check if a player has won
    def check_winner(player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if input_string[i] == input_string[i + 3] == input_string[i + 6] == player:
                return True
            if input_string[i * 3] == input_string[i * 3 + 1] == input_string[i * 3 + 2] == player:
                return True
        if input_string[0] == input_string[4] == input_string[8] == player:
            return True
        if input_string[2] == input_string[4] == input_string[6] == player:
            return True
        return False

    # Count the number of X's and O's
    num_x = input_string.count("X")
    num_o = input_string.count("O")

    # Check game state based on conditions
    x_wins = check_winner("X")
    o_wins = check_winner("O")

    if (x_wins and o_wins) or abs(num_x - num_o) >= 2:
        print("Impossible")
    elif x_wins:
        print("X wins")
    elif o_wins:
        print("O wins")
    elif "_" not in input_string:
        print("Draw")
    else:
        print("Game not finished")


