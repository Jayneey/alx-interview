#!/usr/bin/env python3
import sys

def nqueens(n):
    def is_valid(board, row, col):
        for r, c in board:
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                backtrack(board, row+1)
                board.pop()
                
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = []
    backtrack([], 0)
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)

