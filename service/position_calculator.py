from model import *
from common import *
from service.validation.letter_validator import LetterValidator


class PositionCalculator:

    @classmethod
    def calculate(cls, plateau_input: str, rovers_input: list) -> list:
        p_coord = plateau_input.split()
        x = int(p_coord[0])
        y = int(p_coord[1])
        Plateau.initialize(x, y)
        final_positions = []
        for rover_input in rovers_input:
            validation_result = LetterValidator.validate(rover_input)
            if validation_result.status == Util.FAIL:
                continue
            init_position = rover_input[0].split()
            mov_cmd = rover_input[1]
            rover = cls.__init_rover(init_position)
            rover.process(mov_cmd)
            final_positions.append(rover.current_position)
        return final_positions

    @classmethod
    def __init_rover(cls, init_position: list) -> Rover:
        position = Position(int(init_position[0]), int(init_position[1]))
        direction = Util.DIRECTIONS[init_position[2]]
        rover = Rover()
        rover.set_position(position, direction)
        return rover
