import random

# Define symbols
WALL = "▓"
START = "S"
END = "E"
OPEN_SPACE = "◌"
PATH = "◍"

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def generate_maze(n, wall_prob=0.3):
    maze = [[WALL for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    end = (n - 1, n - 1)

    maze[start[0]][start[1]] = START
    maze[end[0]][end[1]] = END

    # Randomly add walls to the maze
    for i in range(n):
        for j in range(n):
            if random.random() < wall_prob:
                maze[i][j] = WALL

    # Randomly generate a path from start to end
    path_generated = generate_random_path(maze, start, end)
    return maze

def generate_random_path(maze, start, end):
    x, y = start
    maze[x][y] = OPEN_SPACE
    while (x, y) != end:
        valid_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(valid_moves)

        move_made = False
        for dx, dy in valid_moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == WALL:
                maze[new_x][new_y] = OPEN_SPACE
                x, y = new_x, new_y
                move_made = True
                break

        if not move_made:
            return False

    return True

def main():
    print("Welcome to the Maze Generator and Pathfinder!")

    while True:
        try:
            n = int(input("Enter the size of the maze (e.g., 5): "))
            if n <= 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer greater than 1.")

    maze = generate_maze(n)

    while True:
        print("\nGenerated Maze:")
        print_maze(maze)

        print("\nOptions:")
        print("1. Print the Path")
        print("2. Generate Another Maze")
        print("3. Exit the Game")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            if generate_random_path(maze, (0, 0), (n - 1, n - 1)):
                print("Path found!")
                print("\nMaze with Path:")
                print_maze(maze)
            else:
                print("No path found.")

        elif choice == "2":
            # Generate another maze
            maze = generate_maze(n)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
