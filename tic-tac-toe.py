from os import system
import random

test_board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    system("cls")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Choose your marker ( X or O ): ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark)

def choose_first():
    turn = random.randint(1,2)
    if turn == 1:
        return "Player 1"
    else:
        return "Player 2"
print(choose_first())
