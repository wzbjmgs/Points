import unittest

from mock import Mock

from points.src.common.util import Util
from nose.tools import assert_equal

from points.src.model.plateau import Plateau
from points.src.model.position import Position
from points.src.model.rover import Rover


class TestRover(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rover = Rover()
        position = Position(1, 2)
        heading = Util.DIRECTIONS.get("N")
        cls.rover.set_position(position, heading)

    def test_process_inputCmd(self):
        command = "LMLMLMLMM"
        Plateau.is_cell_available = Mock(return_value=True)
        Plateau.update_cell = Mock(return_value=None)
        self.rover.process(command)
        current_position = self.rover.current_position

        assert_equal("1 3 N", current_position)
        Plateau.update_cell.assert_called_once()
