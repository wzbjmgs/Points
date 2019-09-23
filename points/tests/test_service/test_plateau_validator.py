import unittest

from nose.tools import assert_equal
from points.src.common.util import Util
from points.src.service.validation.plateau_validator import PlateauValidator


class TestPlateauValidator(unittest.TestCase):

    def test_validate_inputCoord(self):
        plateau_input = "5 5"
        validation_result = PlateauValidator.validate(plateau_input)

        assert_equal(Util.SUCCESS, validation_result.status)
        assert_equal("", validation_result.message)

    def test_validate_inputEmptyCoord(self):
        plateau_input = ""
        result = PlateauValidator.validate(plateau_input)

        assert_equal(Util.FAIL, result.status)
        assert result.message != ""

    def test_validate_inputPartCoord(self):
        plateau_input = "5"
        result = PlateauValidator.validate(plateau_input)

        assert_equal(Util.FAIL, result.status)
        assert result.message != ""

    def test_validate_inputLetterCoord(self):
        plateau_input = "A 5"
        result = PlateauValidator.validate(plateau_input)

        assert_equal(Util.FAIL, result.status)
        assert result.message != ""

    def test_validate_inputNegativeCoord(self):
        plateau_input = "-1 5"
        result = PlateauValidator.validate(plateau_input)

        assert_equal(Util.FAIL, result.status)
        assert result.message != ""
