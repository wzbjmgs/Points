import logging
import ast
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from points.src.configuration.log_config import setup_logging
from points.src.common.util import Util
from points.src.exception.validation_exception import ValidationException
from points.src.service.position_calculator import PositionCalculator
from points.src.service.validation.plateau_validator import PlateauValidator

__author__ = 'Jayden'

log = logging.getLogger(__name__)


def calculate_rover_position(plateau_input, rovers_input):
    validation_result = PlateauValidator.validate(plateau_input)
    if validation_result.status == Util.FAIL:
        raise ValidationException(validation_result.message)

    final_positions = PositionCalculator.calculate(plateau_input, rovers_input)
    return final_positions


def main(argv):
    setup_logging()
    # argv receive arguments when using shell script start application
    plateau_input = ""
    rovers_input = []
    if len(argv) != 3:
        plateau_input = "5 5"
        rovers_input = ast.literal_eval(
            "[['1 2 N', 'LMLMLMLMM'], ['3 3 E', 'AMMRMMRMRRM']]")
    else:
        plateau_input = argv[1]
        rovers_input = ast.literal_eval(argv[2])

    return calculate_rover_position(plateau_input, rovers_input)


if __name__ == '__main__':
    exit(main(sys.argv))
