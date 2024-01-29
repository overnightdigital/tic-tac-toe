def print_board(board):
    """Print the current board state."""
    for row in board:
        print("|".join(row))
        print("-" * 5)