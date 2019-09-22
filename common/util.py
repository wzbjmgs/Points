class Util(object):

    SUCCESS = "OK"
    FAIL = "fail"

    VALID_COMMANDS = {
        'M': 'move',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    DIRECTIONS = {
        'E': 1,
        'S': 2,
        'W': 3,
        'N': 4,
    }

    @staticmethod
    def is_int(number):
        try:
            int(number)
        except ValueError:
            return False
        return True
