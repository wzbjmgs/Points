import os
import sys
import logging
import ast

sys.path.append(os.path.dirname(sys.path[0]))

from common.util import Util
from exception import ValidationException
from service.position_calculator import PositionCalculator
from service.validation.plateau_validator import PlateauValidator

__author__ = 'Jayden'

log = logging.getLogger(__name__)


def calculate_rover_position(plateau_input: str, rovers_input: list) -> list:
    validation_result = PlateauValidator.validate(plateau_input)
    if validation_result.status == Util.FAIL:
        raise ValidationException(validation_result.message)
    final_positions = PositionCalculator.calculate(plateau_input, rovers_input)
    return final_positions


def main(argv):
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
    rovers_input = ast.literal_eval(argv[2])
    response = calculate_rover_position(argv[1], rovers_input)
    return response


if __name__ == '__main__':
    exit(main(sys.argv))

