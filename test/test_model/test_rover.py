from mock import Mock

from model import *
from common import Util
from nose.tools import assert_equal


class TestRover:

    def setUp(self):
        global rover
        rover = Rover()
        position = Position(1, 2)
        heading = Util.DIRECTIONS.get("N")
        rover.set_position(position, heading)


    def test_process_inputCmd(self):
        command = "LMLMLMLMM"
        Plateau.is_cell_available = Mock(return_value=True)
        Plateau.update_cell = Mock(return_value=None)
        rover.process(command)
        current_position = rover.current_position

        assert_equal("1 3 N", current_position)
        Plateau.update_cell.assert_called_once()
