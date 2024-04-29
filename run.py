# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# This code is from a prievius git hub template which 
# I realise was the wrong one. I copied it here, read more about it in the README file

import random
#while True:
def main():
    print("Select the board size:")
    print("1. small: 3x3")
    print("2. medium: 4x4")
    print("3. large: 5x5")
    choice = int(input("Enter your choice (1 for small, 2 for medium, 3 for large): "))

    sizes = {1: (3, 3), 2: (4, 4), 3: (5, 5)}
    rows, columns = sizes.get(choice, (3, 3))

    board = [[' ' for _ in range(columns)] for _ in range(rows)]
    
    print("Current board:")
    for row in board:
        print('|'.join(row))
        print('-' * (len(row) * 2 - 1))

    moves = 0
    while moves < rows * columns:
            row_input = random.randint(0, rows -1)
            col_input = random.randint(0, columns -1)

            if board[row_input][col_input] == ' ':
                board[row_input][col_input] = 'X'

                checkld = check_ldiagonal(board)
                checkrd = check_rdiagonal(board)

                if checkld == 0 and checkrd == 0:
                    print("Nobody wins")
                elif checkld == 'X' or checkrd == 'X':
                    print("Player wins")
                    break
                elif checkld == 'O' or checkrd == 'O':
                    print("Computer wins")
                    break
                if check_rows_and_col(board):
                    print("Player wins")
                    break
                else:
                    print("Computer wins")
                    break

            board[row_input][col_input] = ' '
            moves += 1

    if moves == rows * columns:
        print("No space left!")

def check_ldiagonal(arr):
    ld = arr[0][0]
    for row in range(1, len(arr)):
        if ld != arr[row][row]:
            return 0
    return ld

def check_rdiagonal(arr):
    rd = arr[0][len(arr) - 1]
    for i in range(1, len(arr)):
        if rd != arr[i][len(arr) - 1 - i]:
            return 0
    return rd

def check_rows_and_col(arr):
    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(arr)):
            col = [row[j] for row in arr]
            if len(set(row)) == 1 or len(set(col)) == 1:
                return True
    return False

if __name__ == "__main__":
    main()
