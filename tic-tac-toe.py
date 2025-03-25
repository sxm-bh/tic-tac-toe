from os import system

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
    pass