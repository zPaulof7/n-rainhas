import unittest
from src.eight_queens import generate_random_board, calculate_heuristic, climb, hill_climbing

class EightQueensTest(unittest.TestCase):

    def test_generate_random_board(self):
        board = generate_random_board()
        assert (len(board) == 8)
       
    def test_heuristic_all_queens_attacking(self):
        board = [0,0,0,0,0,0,0,0]
        assert(calculate_heuristic(board) == 28)

    def test_heuristic_no_queens_attacking(self):
        board = [0, 6, 3, 5, 7, 1, 4, 2]
        assert(calculate_heuristic(board) == 0)
        
        board2 = [4, 2, 0, 6, 1, 7, 5, 3]
        assert(calculate_heuristic(board) == 0)

    def test_heuristic_random_attacks(self):
        board = [0, 2, 2, 6, 2, 3, 1, 1]
        assert(calculate_heuristic(board) == 7)

    def test_climb_progress(self):
        board = generate_random_board()
        heuristic = calculate_heuristic(board)
        
        new_board = climb(board)
        new_heuristic = calculate_heuristic(new_board)

        assert (new_heuristic <= heuristic)

    def test_one_step_left_climbing_hill(self):
        board = [0, 6, 3, 5, 7, 7, 4, 2]
        solution = hill_climbing(board)

        assert (solution == [0, 6, 3, 5, 7, 1, 4, 2])

