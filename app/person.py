from abc import ABCMeta


class Person:
    __metaclass__ = ABCMeta

    def __init__(self, name, position, accommodate='No'):
        self.name = name
        self.position = position
        self.accommodate = accommodate

