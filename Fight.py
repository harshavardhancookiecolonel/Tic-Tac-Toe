# Initialize an empty game board
game_board = ["_" for _ in range(9)]

# Function to display the game board
def display_board():
    print("---------")
    for i in range(0, 9, 3):
        row = game_board[i:i + 3]
        print("|", " ".join(row), "|")
    print("---------")

# Function to check if a player has won
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if game_board[i] == game_board[i + 3] == game_board[i + 6] == player:
            return True
        if game_board[i * 3] == game_board[i * 3 + 1] == game_board[i * 3 + 2] == player:
            return True
    if game_board[0] == game_board[4] == game_board[8] == player:
        return True
    if game_board[2] == game_board[4] == game_board[6] == player:
        return True
    return False

# Function to check if the game is over
def is_game_over():
    x_wins = check_winner("X")
    o_wins = check_winner("O")
    if x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif "_" not in game_board:
        print("Draw")
        return True
    return False

# Display the initial empty game board
display_board()

# Game loop
current_player = "X"
while True:
    # Get user input for the cell coordinates
    move = input(f"Player {current_player}, enter the row and column (e.g., '1 2'): ")
    try:
        row, col = map(int, move.split())
    except ValueError:
        print("Invalid input. Please enter row and column as two space-separated numbers.")
        continue

    # Check if the input is valid
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid input. Row and column must be between 1 and 3.")
        continue

    index = (row - 1) * 3 + (col - 1)

    if game_board[index] != "_":
        print("Invalid move. The cell is already occupied.")
        continue

    # Update the game board with the player's move
    game_board[index] = current_player

    # Display the updated game board
    display_board()

    # Check if the game is over
    if is_game_over():
        break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"
