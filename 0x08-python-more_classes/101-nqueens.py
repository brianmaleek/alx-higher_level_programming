#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    if row == N:
        solutions.append(board.copy())
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)
                board[row] = -1


def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


# Main program
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [-1] * N
solutions = []

solve_nqueens(board, 0)
print_solutions(solutions)
