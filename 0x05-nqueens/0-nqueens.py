
#!/usr/bin/python3
"""_summary_
"""

import sys


def print_solution(solution):
    """_summary_
    Args:
        solution (_type_): _description_
    """
    for pos in solution:
        print(pos, end=", ")
    print()


def is_safe(board, row, col):
    """_summary_
    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """_summary_
    Args:
        board (_type_): _description_
        row (_type_): _description_
        n (_type_): _description_
    """
    if row == n:
        print_solution([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """_summary_
    Args:
        n (_type_): _description_
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    """_summary_
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
