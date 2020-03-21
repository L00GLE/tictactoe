import sys
from ttc_check import GameCheck
from ttc_exit import Exit

print("Welcome to Extreme Tic-Tac-Toe!")

theBoard = {'a0': ' ', 'a1': ' ', 'a2': ' ', 'a3': ' ', 'a4': ' ',
            'b0': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'b4': ' ',
            'c0': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' ', 'c4': ' ',
            'd0': ' ', 'd1': ' ', 'd2': ' ', 'd3': ' ', 'd4': ' ',
            'e0': ' ', 'e1': ' ', 'e2': ' ', 'e3': ' ', 'e4': ' ',
            }

def printBoard(board):
    """Initialize game board."""
    print(board['a0'] + '|' + board['a1'] + '|' + board['a2'] + '|' + board['a3'] + '|' + board['a4'])
    print('-+-+-' + '+-+-')
    print(board['b0'] + '|' + board['b1'] + '|' + board['b2'] + '|' + board['b3'] + '|' + board['b4'])
    print('-+-+-' + '+-+-')
    print(board['c0'] + '|' + board['c1'] + '|' + board['c2'] + '|' + board['c3'] + '|' + board['c4'])
    print('-+-+-' + '+-+-')
    print(board['d0'] + '|' + board['d1'] + '|' + board['d2'] + '|' + board['d3'] + '|' + board['d4'])
    print('-+-+-' + '+-+-')
    print(board['e0'] + '|' + board['e1'] + '|' + board['e2'] + '|' + board['e3'] + '|' + board['e4'])


turn = "X"
for turns in range(24):
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "0"
    else:
        turn = "X"

winners = GameCheck()
print(winners.horizontal_winners())

