import unittest
import sudoku
import numpy as np

unittest.TestLoader.sortTestMethodsUsing = None



class SudokuTest(unittest.TestCase):
    test_board = sudoku.Board(3)


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
    

    def testCheckValidColumn(self):
        # Create column of 1-9 in the left column
        for i in range(9):
            self.test_board.set_value(i,0,i+1)
        # Check that the valid column is recognized as valid
        self.assertTrue(self.test_board.validate_column(0))
    

    def testCheckInvalidColumn(self):
        self.assertFalse(self.test_board.validate_column(1))
    

    def testCheckValidSquare(self):
        # Create a valid square in square 4
        self.test_board.set_value(3,3,1)
        self.test_board.set_value(3,4,2)
        self.test_board.set_value(3,5,3)
        self.test_board.set_value(4,3,4)
        self.test_board.set_value(4,4,5)
        self.test_board.set_value(4,5,6)
        self.test_board.set_value(5,3,7)
        self.test_board.set_value(5,4,8)
        self.test_board.set_value(5,5,9)
        # Check that the valie square is recognized as valid
        self.assertTrue(self.test_board.validate_square(4))
    

    def testCheckInvalidSquare(self):
        self.assertFalse(self.test_board.validate_square(0))
    

    def testCheckGetUnalteredSquare(self):
        s = self.test_board.get_square(8)
        z = np.zeros(9, dtype='int')
        for i in range(9):
            self.assertEqual(s[i], z[i])
    

    def testCheckGetAlteredSquare(self):
        # Create a valid square in square 4
        self.test_board.set_value(3,3,1)
        self.test_board.set_value(3,4,2)
        self.test_board.set_value(3,5,3)
        self.test_board.set_value(4,3,4)
        self.test_board.set_value(4,4,5)
        self.test_board.set_value(4,5,6)
        self.test_board.set_value(5,3,7)
        self.test_board.set_value(5,4,8)
        self.test_board.set_value(5,5,9)
        # Check that each value has been changed
        s = self.test_board.get_square(4)
        r = np.arange(1,10,dtype='int')
        for i in range(9):
            self.assertEqual(s[i], r[i])



if __name__ == '__main__':
    unittest.main()