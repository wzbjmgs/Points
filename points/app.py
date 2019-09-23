import logging

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
    print(final_positions)
    return final_positions


def main():
    log_format= "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
    plateau_input = "5 5"
    rovers_input = []
    rone_init_position = "1 2 N"
    rone_cmd = "LMLMLMLMM"
    rtwo_init_position = "3 3 E"
    rtwo_cmd = "MMRMMRMRRM"
    rover_one = [rone_init_position, rone_cmd]
    rover_two = [rtwo_init_position, rtwo_cmd]
    rovers_input.append(rover_one)
    rovers_input.append(rover_two)
    calculate_rover_position(plateau_input, rovers_input)

if __name__ == '__main__':
    main()
