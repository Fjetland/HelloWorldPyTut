import random


def rand_dice():
    return random.randint(1, 6)


class Dice:
    def __init__(self):
        self.values = (rand_dice(), rand_dice())

    def roll(self):
        self.values = (rand_dice(), rand_dice())
        return self.values

    def get_dices(self):
        return self.values