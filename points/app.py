from service.position_calculator import PositionCalculator
from service.validation import *
from exception.validation_exception import ValidationException

__author__ = 'Jayden'

log = logging.getLogger(__name__)


def calculate_rover_position(plateau_input: str, rovers_input: list) -> list:
    validation_result = PlateauValidator.validate(plateau_input)
    if validation_result.status == Util.FAIL:
        raise ValidationException(validation_result.message)
    final_positions = PositionCalculator.calculate(plateau_input, rovers_input)
    print(final_positions)
    return final_positions


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    urcoordintes = "5 5"
    roverList = []
    roverOneStartPosition = "1 2 N"
    roverOneCommand = "LMLMLMLMM"
    roverTwoStartPosition = "3 3 E"
    roverTwoCommand = "MMRMMRMRRM"
    roverOne = [roverOneStartPosition, roverOneCommand]
    roverTwo = [roverTwoStartPosition, roverTwoCommand]
    roverList.append(roverOne)
    roverList.append(roverTwo)
    calculate_rover_position(urcoordintes, roverList)
