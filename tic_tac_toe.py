# Import os module to access the system functionality for clearing the console window (using system("cls"))
from os import system
# Import random module to generate a random turn (which player goes first)
import random

# Initialize test_board as a list with 10 elements (index 0 is unused) including placeholders for player markers ('X' and 'O')
test_board = ['#','X','O','X','O','X','O','X','O','X']

# display_board function clears the console and displays the current state of the board. It formats the print output in a grid to represent the Tic-Tac-Toe layout
def display_board(board):
    system("cls")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

# player_input function prompts the player to choose their marker, ensuring they select either 'X' or 'O'. It returns a tuple that shows the chosen marker for Player 1 and the other marker for Player 2.
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Choose your marker ( X or O ): ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# place_marker function places the player's marker on the board at a specified position
def place_marker(board, marker, position):
    board[position] = marker

# win_check function checks all possible winning combinations (3 in a row vertically, horizontally, or diagonally) to see if the current player has achieved a win
def win_check(board, mark):
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark)

# choose_first function randomly decides which player goes first in the game
def choose_first():
    turn = random.randint(1,2)
    if turn == 1:
        return "Player 1"
    else:
        return "Player 2"
print(choose_first())
