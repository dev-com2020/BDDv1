import random

_payment = ['card', 'cash']


def _types():
    return _payment[1]


class Payment():
    def __init__(self):
        self.type = []

    def card(self):
        self.type = [_types()]
