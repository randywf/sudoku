import unittest
import sudoku
import numpy as np

class SudokuTest(unittest.TestCase):
    test_board = sudoku.Board(3)


    def test_init(self):
        pass


    def testCheckSetValue(self):
        self.test_board.set_value(0,0,9)
        self.assertEqual(self.test_board.board[0,0], 9)
    

    def testCheckValidRow(self):
        # Create row of 1-9 in the top row
        for i in range(9):
            self.test_board.set_value(0,i,i+1)
        # Check that the valid row is recognized as valid
        self.assertTrue(self.test_board.validate_row(0))
    
    
    def testCheckInvalidRow(self):
        self.assertFalse(self.test_board.validate_row(1))
    


if __name__ == '__main__':
    unittest.main()