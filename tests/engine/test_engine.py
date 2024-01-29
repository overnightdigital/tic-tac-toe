import unittest

from src.engine.engine import init_board, check_win, check_draw, check_move, make_move, run_game

class TestEngine(unittest.TestCase):
    def test_initialize_board(self):
        """Game board is correctly initialized"""
        board = init_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)
            for cell in row:
                self.assertEqual(cell, " ")

    def test_win_scenarios(self):
        # Winning scenario row
        board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(check_win(board, 'X'))

        # Winning scenario column
        board = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
        self.assertTrue(check_win(board, 'O'))

        # Winning scenario diagonal
        board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_win(board, 'X'))

        # Non-winning scenario
        board = [['X', 'O', ' '], ['O', 'X', 'O'], ['O', 'X', ' ']]
        self.assertFalse(check_win(board, 'X'))

    def test_draw_scenario(self):
        # Draw scenario
        board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(check_draw(board))

        # Non-draw scenario
        board = [['X', ' ', 'X'], [' ', 'O', ' '], [' ', ' ', ' ']]
        self.assertFalse(check_draw(board))

    def test_if_valid_moves(self):
        board = [['X', 'O', 'X'], [' ', 'X', ' '], [' ', ' ', 'O']]
        self.assertTrue(check_move(board, (1, 0)))
        self.assertTrue(check_move(board, (1, 2)))
        self.assertTrue(check_move(board, (2, 0)))
        self.assertTrue(check_move(board, (2, 1)))
        self.assertFalse(check_move(board, (0, 1)))
        self.assertFalse(check_move(board, (0, 2)))

    def test_make_move(self):
        board = init_board()
        make_move(board, (0, 0), 'X')
        self.assertEqual(board[0][0], 'X')

    def test_run_game(self):
        try:
            run_game()
        except Exception as e:
            self.fail(f"game raised an exception: {e}")
