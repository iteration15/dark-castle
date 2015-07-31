from constants import *

class Hero(object):
    def __init__(self):
        self.level = 1
        self.stats = {
            'strength': 1,
            'attack': 1,
            'defense': 5
        }
        self.current_hp = 10
        self.name = "Hero"
        self.equipped = {}
