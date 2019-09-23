import unittest
from mock import Mock
from nose.tools import assert_equal

from points.src.common.util import Util
from points.src.model.rover import Rover
from points.src.model.validation_result import ValidationResult
from points.src.service.position_calculator import PositionCalculator
from points.src.service.validation.position_validator import PositionValidator


class TestPositionCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rovers = []
        rone_init_position = "1 2 N"
        rone_cmd = "LMLMLMLMM"
        rtwo_init_position = "3 3 E"
        rtwo_cmd = "MMRMMRMRRM"
        rover_one = [rone_init_position, rone_cmd]
        rover_two = [rtwo_init_position, rtwo_cmd]
        cls.rovers.append(rover_one)
        cls.rovers.append(rover_two)
        cls.plateau = "5 5"

    def setUp(self):
        self.validate = PositionValidator.validate
        self.validation_result = ValidationResult()

    def test_calculate_validationSuccess(self):
        PositionValidator.validate = Mock(return_value=self.validation_result)
        Rover.process = Mock(return_value=None)
        Rover.current_position = Mock(return_value="1 2 N")
        Rover.set_position = Mock(return_value=None)

        final_positions = PositionCalculator.calculate(self.plateau,
                                                       self.rovers)

        assert_equal(2, len(final_positions))

    def test_calculate_validationFail(self):
        self.validation_result.status = Util.FAIL
        PositionValidator.validate = Mock(return_value=self.validation_result)

        final_positions = PositionCalculator.calculate(self.plateau,
                                                       self.rovers)

        assert_equal(0, len(final_positions))

    def tearDown(self):
        PositionValidator.validate = self.validate
