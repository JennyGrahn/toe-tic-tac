# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# This code is from a prievius git hub template which 
# I realise was the wrong one. I copied it here, read more about it in the README file
import random  # Importing the random module for generating random moves.

# Options for the user to decide the board size.
USER_OPTIONS = """
Select the board size:
    1. small: 3x3
    2. medium: 4x4
    3. large: 5x5
"""

# Function to get the board size devided by the user.
def get_board_size():
    sizes = {1: (3, 3), 2: (4, 4), 3: (5, 5)}
    while True:
        print(USER_OPTIONS)
        try:
            choice = int(input("Enter your choice (1 for small, 2 for medium, 3 for large):"))
            if choice not in sizes:
                raise ValueError
            return sizes[choice]
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3")

# Function to print the current state of the board.
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (len(row) * 2 - 1))

# Function for players turn.
def get_player_turn(size):
    while True:
        try:
            x, y = map(int, input(f"Enter the row and column you want (0-{size-1}, 0-{size-1}): ").split())
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print(f"Invalid input. Please enter row and column values between 0 and {size-1}.")
        except ValueError:
            print("Invalid input. Please enter integer values.")

# Function to check if there's a winner.
def check_winner(board):
    
    checkld = check_ldiagonal(board)
    checkrd = check_rdiagonal(board)
    check_rows = check_rows_and_col(board)
    check_columns = check_columns(board)
    
    # Determine the winner based on the checks.
    if checkld == 0 and checkrd == 0 and not check_rows and not check_columns:
        return "Nobody wins"
    elif checkld == 'X' or checkrd == 'X' or check_rows or check_columns:
        return "Player wins"
    elif checkld == 'O' or checkrd == 'O':
        return "Computer wins"
    else:
        return "Computer wins"

# Function to check the left diagonal of the board for a winner.
def check_ldiagonal(arr):
    ld = arr[0][0]
    for row in range(1, len(arr)):
        if ld != arr[row][row]:
            return 0
    return ld

# Function to check the right diagonal of the board for a winner.
def check_rdiagonal(arr):
    rd = arr[0][len(arr) - 1]
    for i in range(1, len(arr)):
        if rd != arr[i][len(arr) - 1 - i]:
            return 0
    return rd

# Function to check rows and columns of the board for a winner.
def check_rows_and_col(arr):
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(arr)):
            col = [row[j] for row in arr]
            if len(set(row)) == 1 or len(set(col)) == 1:
                return True
    return False

# Function to check columns of the board for a winner.
def check_columns(arr):
    for col in range(len(arr[0])):
        column = [row[col] for row in arr]
        if len(set(column)) == 1 and column[0] != ' ':
            return True
    return False

# Main function to run the game.
def main():
    rows, columns = get_board_size()
    board = [[' ' for _ in range(columns)] for _ in range(rows)]

    print("Current board:")
    print_board(board)

    moves = 0 
    # Loop until all spaces on the board are filled or there's a winner.
    while moves < rows * columns:
        row_input = random.randint(0, rows -1)
        col_input = random.randint(0, columns -1)

        if board[row_input][col_input] == ' ':
            board[row_input][col_input] = 'X'

            # Check if there's a winner after the move.
            print(check_winner(board))
            break

        board[row_input][col_input] = ' '
        moves += 1

    # If all spaces are filled without a winner, print a message indicating no space left.
    if moves == rows * columns:
        print("No space left!")

# Entry point of the program.
if __name__ == "__main__":
    main()








