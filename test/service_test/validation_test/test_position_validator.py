import unittest
import numpy as np
from common import Util
from model import Plateau
from service.validation.position_validator import PositionValidator


class TestPositionValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Plateau.matrix = np.ones((5, 5), dtype=bool)

    def test_validate_inputRoverData(self):
        init_position = "1 2 N"
        command = "LMLMLMLMM"
        rover_input = [init_position, command]
        result = PositionValidator.validate(rover_input)

        self.assertEqual(Util.SUCCESS, result.status)
        self.assertEqual("", result.message)

    def test_validate_inputEmptyData(self):
        init_position = ""
        command = "LMLMLMLMM"
        rover_input = [init_position, command]
        result = PositionValidator.validate(rover_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_inputOutBoundData(self):
        init_position = "7 20 N"
        command = "LMLMLMLMM"
        rover_input = [init_position, command]
        result = PositionValidator.validate(rover_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_inputLetterPosition(self):
        init_position = "A A N"
        command = "LMLMLMLMM"
        rover_input = [init_position, command]
        result = PositionValidator.validate(rover_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_missDirection(self):
        init_position = "1 2"
        command = "LMLMLMLMM"
        rover_input = [init_position, command]
        result = PositionValidator.validate(rover_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")
