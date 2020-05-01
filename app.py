import random

from dice import Dice

members = ["John", "Bob", "Sophie"]

leader = random.choice(members)
print(leader)

dices = Dice()
print(dices.values)
dices.roll()
print(dices.values)