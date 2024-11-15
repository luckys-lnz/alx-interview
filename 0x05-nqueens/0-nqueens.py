#!/usr/bin/python3
import sys


def print_solution(board):
    """Prints the solution in the required format"""
    print([[i, board[i]] for i in range(len(board))])


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        # Check if two queens share the same column or diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, board, row):
    """Solves the N queens problem using backtracking"""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)
            board[row] = -1  # Backtrack


def main():
    """Main function that parses input and invokes the solver"""
    if len(sys.argv) != 2:
        print("Usage: N queens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n  # Create an empty board of size n
    solve_nqueens(n, board, 0)


if __name__ == "__main__":
    main()
