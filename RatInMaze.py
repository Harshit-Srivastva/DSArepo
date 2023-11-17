def is_valid_move(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, solution, n):
    # Check if the rat has reached the destination
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True

    # Check if the move is valid
    if is_valid_move(maze, x, y, n):
        solution[x][y] = 1

        # Move right
        if solve_maze_util(maze, x, y + 1, solution, n):
            return True

        # Move down
        if solve_maze_util(maze, x + 1, y, solution, n):
            return True

        # If neither right nor down leads to the solution, backtrack
        solution[x][y] = 0
        return False

    return False

def solve_maze(maze):
    n = len(maze)

    # Create a solution matrix initialized to 0
    solution = [[0 for _ in range(n)] for _ in range(n)]

    # Start solving the maze from the top-left corner
    if solve_maze_util(maze, 0, 0, solution, n):
        return solution
    else:
        return None

# Example: Solve a maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)

if result:
    print("Solution:")
    for row in result:
        print(row)
else:
    print("No solution exists.")
