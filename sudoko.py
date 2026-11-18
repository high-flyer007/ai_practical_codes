
# Sudoku Solver using Backtracking and Constraint Propagation

# 0 represents an empty cell
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def get_candidates(board, row, col):
    # Initially, all numbers are possible
    candidates = set(range(1, 10))

    # Remove numbers already present in the row
    candidates -= set(board[row])

    # Remove numbers already present in the column
    candidates -= {board[r][col] for r in range(9)}

    # Find the starting position of the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    # Remove numbers already present in the 3x3 box
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            candidates.discard(board[r][c])

    return candidates


def find_empty_cell(board):
    # Find the first empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None


def solve_sudoku(board):
    # Find an empty cell
    empty = find_empty_cell(board)

    # No empty cells means the puzzle is solved
    if empty is None:
        return True

    row, col = empty

    # Apply constraint propagation
    candidates = get_candidates(board, row, col)

    # Try every possible value
    for num in sorted(candidates):
        board[row][col] = num

        # Recursively solve the remaining puzzle
        if solve_sudoku(board):
            return True

        # If unsuccessful, undo the assignment
        board[row][col] = 0

    # No candidate leads to a solution
    return False


def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) for num in row))


print("Original Sudoku:")
print_sudoku(sudoku)

if solve_sudoku(sudoku):
    print("\nSolved Sudoku:")
    print_sudoku(sudoku)
else:
    print("\nNo solution exists.")
