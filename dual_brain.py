class DualBrain:
    def __init__(self):
        self.priority_elevator = "right"

    def choose_side(self, human_location, right_location, left_location):

        if abs(right_location - human_location) > abs(left_location - human_location):
            self.priority_elevator = "left"
