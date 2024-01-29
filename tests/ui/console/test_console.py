import unittest
import io
import sys

from src.ui.console.console import print_board

class TestConsole(unittest.TestCase):
     def test_print_board(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', 'X']]

        expected_output = "X|O|X\n-----\nO|X|O\n-----\n | |X\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        print_board(board)

        # Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)