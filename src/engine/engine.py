def init_board():
    """Create a 3x3 matrix represented as a list of lists."""
    return [[" " for _ in range(3)] for _ in range(3)]


def check_win(board, player):
    """Check if the given player has won the game."""
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    """Check if the game is a draw."""
    return all(all(cell != " " for cell in row) for row in board)