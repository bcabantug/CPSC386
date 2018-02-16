CPSC 386-01
Project 1: Python Maze
Team Name: CGZ
Team Members:
-Brian Cabantug
-Hancheng Zhou
-Mason Guzman-Sanchez

Introduction: This script generates a 2d maze based on the amount of rows and columns input by the user.
This python script uses the Binary Space Partition Algorithm to generate the portals of the maze and then
outputs the completed maze.

Contents:
-README.txt (aka this file)
-maze_complete.py (maze script)
-eightbyeight.txt (output for 8x8 maze)
-tenbyten.txt (output for 10x10 maze)

External Requirements: None

Setup and Installation:
Install Python3 on local computer to use
Copy the script file to home directory
Navigate to home directory and run using python3 (command: python3 maze_complete.py)

Sample invocation & results:
python3 maze.py 
enter number of row: 4
enter number of col: 4
Portal list (reads as from 0 to 2n):
[4, 5]
[1, 6]
[2, 3]
[1, 4]
[1, 2]
[3, 4]
[3, 2]
[2, 7]
[7, 6]
[6, 3]
[5, 4]
[5, 2]
[7, 4]
[7, 2]
[6, 7]

+ - + - + - + - +
| S             |
+ - +   + - +   +
|           |   |
+ - + - +   + - +
|           |   |
+ - +   + - +   +
|             X |
+ - + - + - + - +

Features: 
-Prints out portal list and maze
-User input for rows and columms

Bugs:
-does not check if input is letter/character that is not a number (will error)
