# ask for user input
row_num = input("enter number of row: ")
col_num = input("enter number of col: ")
row_line = 2 * int(row_num) + 1
col_line = 2 * int(col_num) + 1
# initial maze with 0s
maze = []
for x in range(row_line):
    maze.append(["O"] * col_line)
# mark corners
for x in range(row_line):
    for y in range(col_line):
        if (x%2 == 0) and (y%2 == 0):
            maze[x][y] = '+'
# mark the boarders
for i in range(col_line):
    if i%2 != 0:
        maze[0][i] = '-'
        maze[row_line-1][i] = '-'
for j in range(row_line):
    if j % 2 != 0:
        maze[j][0] = '|'
        maze[j][col_line - 1] = '|'
# mark starting point and ending point
for row in maze:
    maze[1][1] = 'S'
    maze[row_line - 2][col_line - 2] = 'X'


def print_maze(maze):
    for row in maze:
        print(" ".join(row))


if __name__ == "__main__":
    print(maze)
    print_maze(maze)
