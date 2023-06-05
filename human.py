import random

ELEVATOR_FLOORS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11,
                   "12": 12, "13": 13, "R": 14}

class Human:

    def __init__(self):

        self.destination = None
        self.location = None
        self.action = None

    def set_starting_floor(self):
        self.location = random.choice(list(ELEVATOR_FLOORS.values()))
        self.action = "pick up"

    def set_destination_floor(self):
        self.destination = random.choice(list(ELEVATOR_FLOORS.values()))
        self.action = "drop off"