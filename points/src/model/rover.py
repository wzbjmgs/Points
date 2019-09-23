import logging

from points.src.common.util import Util
from .plateau import Plateau


class Rover(object):
    logger = logging.getLogger(__name__)

    __position = ""
    __prv_position = ""
    __direction = Util.DIRECTIONS['N']

    def set_position(self, position, heading):
        self.__position = position
        self.__direction = heading
        self.__prv_position = self.__position

    @property
    def current_position(self):
        return '{} {} {}'.format(self.__position.x, self.__position.y, self.get_direction)

    @property
    def get_direction(self):
        directions = list(Util.DIRECTIONS.keys())
        try:
            direction = directions[self.__direction - 1]
        except IndexError:
            direction = 'N'
        return direction

    def process(self, commands):
        for i in range(len(commands)):
            if not self.process_command(commands[i]):
                self.logger.error(
                    "Id:" + i + " .Rover can't move to next step due to collision or out of safe area, rover will "
                    "stop at current position and abandon the rest commands if there is "
                )
                break
        Plateau.update_cell(self.__position.x, self.__position.y)

    def process_command(self, command) -> bool:
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            if not self.move():
                return False
        else:
            return False
        return True

    def move(self):
        pre_x = self.__position.x
        pre_y = self.__position.y
        if Util.DIRECTIONS['N'] == self.__direction:
            self.__position.y += 1
        elif Util.DIRECTIONS['E'] == self.__direction:
            self.__position.x += 1
        elif Util.DIRECTIONS['S'] == self.__direction:
            self.__position.y -= 1
        elif Util.DIRECTIONS['W'] == self.__direction:
            self.__position.x -= 1
        if not Plateau.is_cell_available(self.__position.x, self.__position.y):
            self.__position.x = pre_x
            self.__position.y = pre_y
            return False
        self.logger.info("Rover move forward one step and current position are: " + str(self.__position.x) + ":" + str(self.__position.y))
        return True

    def turn_left(self):
        self.logger.info("rover turn left and current direction is: " + self.get_direction)
        self.__direction = Util.DIRECTIONS['N'] if (self.__direction -1) < Util.DIRECTIONS['E'] else self.__direction - 1

    def turn_right(self):
        self.logger.info("rover turn right and current direction is: " + self.get_direction)
        self.__direction = Util.DIRECTIONS['E'] if (self.__direction + 1) > Util.DIRECTIONS['N'] else self.__direction + 1
