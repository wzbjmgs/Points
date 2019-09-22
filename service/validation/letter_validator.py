from common import Util
from model import ValidationResult
from service.validation.base_validator import BaseValidator
import logging
import re


class LetterValidator(BaseValidator):
    logger = logging.getLogger(__name__)

    @classmethod
    def validate(cls, rover_input: str) -> ValidationResult:
        cls.logger.info("Validate rover input data")
        result = ValidationResult()

        start_position = rover_input[0]
        position_regex = "^[0-9]+ [0-9]+ [ESWN]+$"
        position_match = re.match(position_regex, start_position)
        if not position_match:
            result.status = Util.FAIL
            result.message = "Input rover start position is invalid. Please input two position integer and one letter " \
                             "as one of E S W N"
            return result
        return result
