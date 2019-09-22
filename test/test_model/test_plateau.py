import unittest
from model import Plateau


class TestPlateau(unittest.TestCase):

    def setUp(self):
        x = 5
        y = 5
        Plateau.initialize(x, y)

    def test_initialize_inputCoord(self):
        num_rows = str(len(Plateau.matrix) - 1)
        num_cols = str(len(Plateau.matrix[0]) - 1)
        self.assertEqual(5, int(num_rows))
        self.assertEqual(5, int(num_cols))

    def test_is_cell_available_inputCoord(self):
        x = 5
        y = 5
        Plateau.initialize(x, y)
        Plateau.is_cell_available(x, y)
        self.assertTrue(Plateau.matrix[x][y])

    def test_update_cell_inputCoord(self):
        x = 5
        y = 5
        Plateau.update_cell(x, y)
        self.assertTrue(not Plateau.matrix[x][y])