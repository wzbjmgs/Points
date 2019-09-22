import numpy


class Plateau(object):
    min_width = 0
    min_height = 0
    matrix = []

    @classmethod
    def initialize(cls, width, height):
        cls.width = width + 1
        cls.height = height + 1
        cls.matrix = numpy.ones((cls.width, cls.height), dtype=bool)

    @classmethod
    def is_cell_available(cls, x, y) -> bool:
        return cls.min_width <= x <= cls.width \
               and cls.min_width <= y <= cls.height \
               and not cls.matrix[x][y]

    @classmethod
    def update_cell(cls, x, y):
        cls.matrix[x][y] = False
