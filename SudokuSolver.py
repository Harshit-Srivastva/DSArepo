def is_safe(board, row, col, num):
    # Check if 'num' is not present in current row, current column, and current 3x3 subgrid
    return not any([
        num in board[row],                     # Check row
        num in [board[i][col] for i in range(9)],  # Check column
        num in [board[i][j] for i in range(row - row % 3, row - row % 3 + 3)  # Check subgrid
                for j in range(col - col % 3, col - col % 3 + 3)]
    ])

def find_unassigned_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1  # If no unassigned location is found

def solve_sudoku(board):
    row, col = find_unassigned_location(board)

    # If there is no unassigned location, the puzzle is solved
    if row == -1 and col == -1:
        return True

    # Try digits 1 through 9
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            # Assign the number if it's safe
            board[row][col] = num

            # Recursively attempt to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If assigning the current number doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No solution found for this configuration
    return False

# Example: Solve a Sudoku puzzle
sudoku_board = [
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

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
