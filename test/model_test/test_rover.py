import unittest
from unittest.mock import patch, Mock
from model import *
from common import Util


class TestRover(unittest.TestCase):

    def setUp(self):
        self.rover = Rover()
        position = Position(1, 2)
        heading = Util.DIRECTIONS.get("N")
        self.rover.set_position(position, heading)

    def test_process_inputCmd(self):
        command = "LMLMLMLMM"
        Plateau.is_cell_available = Mock(return_value=True)
        Plateau.update_cell = Mock(return_value=None)
        self.rover.process(command)
        current_position = self.rover.current_position

        self.assertEqual("1 3 N", current_position)
        Plateau.update_cell.assert_called_once()
