import logging
import re

from points.src.main.common.util import Util
from points.src.main.model.plateau import Plateau
from points.src.main.model.validation_result import ValidationResult
from points.src.main.service.validation.base_validator import BaseValidator


class PositionValidator(BaseValidator):
    logger = logging.getLogger(__name__)

    @classmethod
    def validate(cls, rover_input: str) -> ValidationResult:
        cls.logger.info("Validate rover input data")
        result = ValidationResult()
        plateau_matrix = Plateau.matrix
        num_rows = str(len(plateau_matrix) - 1)
        num_cols = str(len(plateau_matrix[0]) - 1)
        start_position = rover_input[0]
        position_regex = "^[0-" + num_rows + "]+ [0-" + num_cols + "]+ [ESWN]+$"
        position_match = re.match(position_regex, start_position)
        if not position_match:
            result.status = Util.FAIL
            result.message = "Input rover initial position is invalid. Rover has be inside plateau. Please input two " \
                             "integer position and one letter as one of E S W N"
            cls.logger.error(result.message)
            return result
        return result
