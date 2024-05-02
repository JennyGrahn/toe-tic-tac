# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# This code is from a prievius git hub template which 
# I realise was the wrong one. I copied it here, read more about it in the README file

import random

USER_OPTIONS = """
Select the board size:
    1. small: 3x3
    2. medium: 4x4
    3. large: 5x5
"""

def minimax(board, depth, max_depth, maxTurn):
    if check_winner(board) == "Player wins":
        return -1
    elif check_winner(board) == "Computer wins":
        return 1
    elif check_winner(board) == "Nobody wins" or depth == max_depth:
        return 0

    if maxTurn:
        max_value = -float('inf')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    minmax_val = minimax(board, depth + 1, max_depth, False)
                    board[i][j] = " "
                    max_value = max(max_value, minmax_val)
        return max_value
    else:
        min_value = float('inf')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    minmax_val = minimax(board, depth + 1, max_depth, True)
                    board[i][j] = " "
                    min_value = min(min_value, minmax_val)
        return min_value

def ai_move(board, max_depth):
    best_move = None
    best_val = -float("inf")

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                board[i][j] = "O"
                minmax_val = minimax(board, 0, max_depth, False)
                board[i][j] = " "
                if minmax_val > best_val:
                    best_move = (i, j)
                    best_val = minmax_val
    return best_move

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

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (len(row) * 2 - 1))

def check_winner(board): 
    checkld = check_ldiagonal(board) 
    checkrd = check_rdiagonal(board) 
    check_rows = check_rows_and_col(board) 
    check_all_columns = check_columns(board) 
    
    print(checkld,checkrd,check_rows,check_all_columns)

    if check_ld == "X" or check_rd == "X" or check_rows or check_columns:
        return "Player wins"
    elif check_ld == "O" or check_rd == "O":
        return "Computer wins"
    elif check_ld == " " and check_rd == " " and not check_rows and not check_columns:
        return "Nobody wins"
    else:
        return "Nobody wins"

def check_ldiagonal(arr):
    ld = arr[0][0]
    for row in range(1, len(arr)):
        if ld != arr[row][row]:
            return " "
    return ld

def check_rdiagonal(arr):
    rd = arr[0][len(arr) - 1]
    for i in range(1, len(arr)):
        if rd != arr[i][len(arr) - 1 - i]:
            return " "
    return rd

def check_rows_and_col(arr):
    for i in range(len(arr)):
        row = arr[i]
        if len(set(row)) == 1 and row[0] != " ":
            return True
    for j in range(len(arr[0])):
        column = [row[j] for row in arr]
        if len(set(column)) == 1 and column[0] != " ":
            return True
    return False

def check_columns(arr):
    for col in range(len(arr[0])):
        column = [row[col] for row in arr]
        if len(set(column)) == 1 and column[0] != ' ':
            return True
    return False

def main():
    rows, columns = get_board_size()
    board = [[' ' for _ in range(columns)] for _ in range(rows)]

    print("Current board:")
    print_board(board)

    moves = 0
    while moves < rows * columns:
        row_input, col_input = players_move(board)

        if board[row_input][col_input] == ' ':
            board[row_input][col_input] = 'X'

            print(check_winner(board))
            move +=1 
            ai = ai_move()
            if moves == rows * columns:
                break
        
        else:
            print("Please Select an empty Slot")
            continue

        board[row_input][col_input] = ' '
        moves += 1

    if moves == rows * columns:
        print("No space left!")

if __name__ == "__main__":
    main()










