import unittest

from common import Util
from service.validation import PlateauValidator


class TestPlateauValidator(unittest.TestCase):

    def test_validate_inputCoord(self):
        plateau_input = "5 5"
        result = PlateauValidator.validate(plateau_input)

        self.assertEqual(Util.SUCCESS, result.status)
        self.assertEqual("", result.message)

    def test_validate_inputEmptyCoord(self):
        plateau_input = ""
        result = PlateauValidator.validate(plateau_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_inputPartCoord(self):
        plateau_input = "5"
        result = PlateauValidator.validate(plateau_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_inputLetterCoord(self):
        plateau_input = "A 5"
        result = PlateauValidator.validate(plateau_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")

    def test_validate_inputNegativeCoord(self):
        plateau_input = "-1 5"
        result = PlateauValidator.validate(plateau_input)

        self.assertEqual(Util.FAIL, result.status)
        self.assertTrue(result.message != "")
