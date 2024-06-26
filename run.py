# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# This code is from a prievius git hub template which 
# I realise was the wrong one. I copied it here, read more about it in the README file

import random  # Importing the random module for generating random moves.
import time
def load_message():
    print("Welcome to Tic Tac Toe!")
    print("Rules:")
    print("1. The game is played on a 3x3, 4x4 and 5x5 grid.")
    print("2. Players take turns marking a square with their symbol (X or O).")
    print("3. The first player to get three, four or five of their symbols in a row (horizontally, vertically, or diagonally) wins.")

    while True:
        user_input = input("When you're ready to start the game, type 'start the game' and press Enter: ")
        if user_input.strip().lower() != 'start the game':
            print("Invalid input. Exiting...")
        else:
            print("Loading Tic Tac Toe game...")
            print("Tic Tac Toe game loaded!")
            break
    

# Options for the user to decide the board size.
USER_OPTIONS = """
Select the board size:
    1. small: 3x3
    2. medium: 4x4
    3. large: 5x5
"""

# Implementing the minimax algorithm.
def minimax(board, depth, max_depth, maxTurn):
    if check_winner(board) == "Player wins":
        return -1
    elif check_winner(board) == "Computer wins":
        return 1
    elif not check_winner(board) or depth == max_depth:
        return 0

    # Maximizing player's turn.
    if maxTurn:
        max_value = -float('inf')
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    minmax_val = minimax(board, depth + 1, max_depth, False)
                    board[i][j] = " "
                    max_value = max(max_value, minmax_val)
        return max_value
    # Minimizing player's turn.
    else:
        min_value = float('inf')
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    minmax_val = minimax(board, depth + 1, max_depth, True)
                    board[i][j] = " "
                    min_value = min(min_value, minmax_val)
        return min_value
    
# Implementing AI move using minimax algorithm.
def ai_move(board,max_depth):
    best_move = None
    best_val = -float("inf")

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "O"
                minmax_val = minimax(board, 0, max_depth, False)
                board[i][j] = " "
                if minmax_val >= best_val:
                    best_move = (i, j)
                    best_val = minmax_val
             
    return best_move


# Allowing player to make a move.
def players_move(board):
    while True:
        try:
            row = int(input('Enter row number: '))
            col = int(input('Enter column number: '))
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                return row, col
            else:
                print("Invalid Move. Please try writing a valid move")
        except ValueError:
            print("Invalid Input. Please enter a whole number")

# Asking the user for the board size.

# Printing the current state of the board.
def print_board(board): 
    for row in board:
        print('|'.join(row))
        print('-' * (len(row) * 2 - 1))

 # Checking for a winner in all possible directions.
def check_winner(board): 
    checkld = check_ldiagonal(board)
    checkrd = check_rdiagonal(board)
    check_all_rows = check_rows(board)
    check_all_columns = check_columns(board)

    if not checkld and not checkrd and not check_all_rows and not check_all_columns:
        for i in board:
            if " " in i:
                return True
        return False 
    elif checkld == 'X' or checkrd == 'X' or check_all_rows == "X" or check_all_columns == "X":
        return "Player wins"
    elif checkld == 'O' or checkrd == 'O' or check_all_rows == "O" or check_all_columns == "O":
        return "Computer wins"
    
# Checking the left diagonal of the board for a winner.
def check_ldiagonal(arr):
    ld = arr[0][0]
    for row in range(1, len(arr)):
        if ld != arr[row][row]:
            return False
    return ld

# Checking the right diagonal of the board for a winner.
def check_rdiagonal(arr):
    rd = arr[0][len(arr) - 1]
    for i in range(1, len(arr)):
        if rd != arr[i][len(arr) - 1 - i]:
            return False
    return rd
 # Checking rows and columns of the board for a winner.

def check_rows(arr):
    for i in range(len(arr)):
        row = arr[i]
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]
    return False

 # Checking columns of the board for a winner.

 
def check_columns(arr):
    for col in range(len(arr[0])):
        column = [row[col] for row in arr]
        if len(set(column)) == 1 and column[0] != ' ':
            return column[0]
    return False
# Main function to run the game.
def main():
    rows, columns = 3,3
    board = [[' ' for _ in range(columns)] for _ in range(rows)]

    print("Current board:")
    print_board(board)

    moves = 0
    while True:
        row_input, col_input = players_move(board)

        if board[row_input][col_input] == ' ':
            board[row_input][col_input] = 'X'
            print_board(board)
            if check_winner(board) == "Player wins":
                print("Player wins")
                break
            moves +=1
            if moves == rows * columns:
                print("It's a tie")
                break

            print("\n Ai making move.........")
            time.sleep(2)
            ai_row,ai_col = ai_move(board,8)
            board[ai_row][ai_col] = 'O'
            print_board(board)
            if check_winner(board) == "Computer wins":
                print("Computer wins!")
                break
            moves +=1
            
          

        
        else:
            print("Please Select an empty Slot")
            continue


if __name__ == "__main__":
    load_message()
    main()
