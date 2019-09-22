import logging
import re
from common import Util
from model import ValidationResult
from service.validation.base_validator import BaseValidator


class PlateauValidator(BaseValidator):
    logger = logging.getLogger(__name__)

    @classmethod
    def validate(cls, plateau_input: str) -> ValidationResult:
        cls.logger.info("Validate plateau input data")
        result = ValidationResult()
        regex = "^[0-9]+ [0-9]+$"
        print(plateau_input)
        match = re.match(regex, plateau_input)
        if not match:
            result.status = Util.FAIL
            result.message = "Plateau input is invalid. Please input two positive integer with white space as separator"
            return result
        return result
