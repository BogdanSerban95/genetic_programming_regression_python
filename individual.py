import sexpdata as spd
import random as rnd


class Individual(object):
    operators = {
        'add': 2,
        'sub': 2,
        'mul': 2,
        'div': 2,
        'pow': 1,
        'sqrt': 1,
        'log': 1,
        'exp': 1,
        'max': 2,
        'ifleq': 4,
        'data': 1,
        'diff': 2,
        'avg': 2
    }

    def __init__(self):
        self.expr = []
        self.fitness = 0

    def random_init(self, height):
        pass

    def mutate(self):
        pass
