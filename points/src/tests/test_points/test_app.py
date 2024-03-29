import unittest
from unittest.mock import Mock

from points.app import calculate_rover_position
from points.src.main.common.util import Util
from points.src.main.exception.validation_exception import ValidationException
from points.src.main.model.validation_result import ValidationResult
from points.src.main.service.position_calculator import PositionCalculator
from points.src.main.service.validation.plateau_validator import PlateauValidator


class TestApp(unittest.TestCase):

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
        cls.final_positions = ["1 2 N", "3 3 E"]

    def setUp(self):
        self.validate = PlateauValidator.validate
        self.calculate = PositionCalculator.calculate
        self.validation_result = ValidationResult()

    def test_calculate_rover_position_validationSuccess(self):
        PlateauValidator.validate = Mock(return_value=self.validation_result)
        PositionCalculator.calculate = Mock(return_value=self.final_positions)
        final_positions = calculate_rover_position(self.plateau, self.rovers)

        self.assertEqual(2, len(final_positions))

    def test_test_calculate_rover_position_validationFail(self):
        self.validation_result.status = Util.FAIL
        self.validation_result.message = "Fail"
        PlateauValidator.validate = Mock(return_value=self.validation_result)
        try:
            calculate_rover_position(self.plateau, self.rovers)
        except ValidationException as ex:
            self.assertEqual("Fail", ex.error_msg)

    def tearDown(self):
        PlateauValidator.validate = self.validate
        PositionCalculator.calculate = self.calculate
