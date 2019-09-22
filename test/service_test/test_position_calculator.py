import unittest
from mock import Mock
from common import Util
from model import *
from service.position_calculator import PositionCalculator
from service.validation.position_validator import PositionValidator


class TestPositionCalculator(unittest.TestCase):

    def setUp(self):
        self.rovers = []
        rone_init_position = "1 2 N"
        rone_cmd = "LMLMLMLMM"
        rtwo_init_position = "3 3 E"
        rtwo_cmd = "MMRMMRMRRM"
        rover_one = [rone_init_position, rone_cmd]
        rover_two = [rtwo_init_position, rtwo_cmd]
        self.rovers.append(rover_one)
        self.rovers.append(rover_two)
        self.plateau = "5 5"
        self.validation_result = ValidationResult()

    def test_calculate_validationSuccess(self):
        PositionValidator.validate = Mock(return_value=self.validation_result)
        Rover.process = Mock(return_value=None)
        Rover.current_position = Mock(return_value="1 2 N")
        Rover.set_position = Mock(return_value=None)

        final_positions = PositionCalculator.calculate(self.plateau, self.rovers)

        self.assertEqual(2, len(final_positions))

    def test_calculate_validationFail(self):
        self.validation_result.status=Util.FAIL
        PositionValidator.validate = Mock(return_value=self.validation_result)

        final_positions = PositionCalculator.calculate(self.plateau, self.rovers)

        self.assertEqual(0, len(final_positions))
