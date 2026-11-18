
N = 8

# Create an empty chessboard
board = [[0 for _ in range(N)] for _ in range(N)]


# Check whether placing a queen is safe
def is_safe(board, row, col):

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Solve the 8-Queens problem using backtracking
def solve_n_queens(board, col):

    # If all columns are filled, solution is found
    if col >= N:
        return True

    # Try every row in the current column
    for row in range(N):

        if is_safe(board, row, col):

            # Place the queen
            board[row][col] = 1

            # Recursively solve the next column
            if solve_n_queens(board, col + 1):
                return True

            # If unsuccessful, remove the queen
            board[row][col] = 0

    return False


# Display the chessboard
def print_board(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
if solve_n_queens(board, 0):
    print("Solution for 8-Queens Problem:")
    print_board(board)
else:
    print("No solution exists.")
