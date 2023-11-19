
import unittest
import pygame as pg
from unittest.mock import patch
from game import TicTacToe, Game, WIN_SIZE, CELL_SIZE

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.game = Game()

    def tearDown(self):
        pg.quit()

    @patch('pygame.mouse.get_pressed', return_value=(1, 0, 0))
    @patch('pygame.mouse.get_pos', return_value=(CELL_SIZE // 2, CELL_SIZE // 2))
    def test_run_game_process(self, mock_mouse_pos, mock_mouse_pressed):
        self.game.tic_tac_toe.run_game_process()
        self.assertEqual(self.game.tic_tac_toe.game_array[0][0], 0)  # Assuming player 0 clicked in the center of the first cell
        self.assertEqual(self.game.tic_tac_toe.player, 1)  # After the first move, the player should be switched

    def test_check_winner(self):
        # Test a winning scenario for 'X'
        self.game.tic_tac_toe.game_array = [[1, 1, 0],
                                            [0, 1, 0],
                                            [1, 0, 1]]
        self.game.tic_tac_toe.check_winner()
        self.assertEqual(self.game.tic_tac_toe.winner, 'X')

        # Test a winning scenario for 'O'
        self.game.tic_tac_toe.game_array = [[0, 1, 0],
                                            [1, 1, 1],
                                            [0, 0, 0]]
        self.game.tic_tac_toe.check_winner()
        self.assertEqual(self.game.tic_tac_toe.winner, 'O')

    def test_draw_objects(self):
        # Assuming X wins
        self.game.tic_tac_toe.game_array = [[1, 1, 0],
                                            [0, 1, 0],
                                            [1, 0, 1]]
        self.game.tic_tac_toe.check_winner()  # Simulating a win
        self.game.tic_tac_toe.draw_objects()
        # Assertions based on how the objects are drawn

    def test_draw_winner(self):
        # Assuming X wins
        self.game.tic_tac_toe.game_array = [[1, 1, 0],
                                            [0, 1, 0],
                                            [1, 0, 1]]
        self.game.tic_tac_toe.check_winner()  # Simulating a win
        self.game.tic_tac_toe.draw_winner()
        # Assertions based on how the winner is drawn

    def test_draw(self):
        # Assuming X wins
        self.game.tic_tac_toe.game_array = [[1, 1, 0],
                                            [0, 1, 0],
                                            [1, 0, 1]]
        self.game.tic_tac_toe.check_winner()  # Simulate a win
        self.game.tic_tac_toe.draw()
        # Assertions based on how the entire screen is drawn

    def test_get_scaled_image(self):
        # Test cases for the get_scaled_image function
        pass

    def test_run(self):
        # Test cases for the run function
        pass

if __name__ == '__main__':
    unittest.main()


