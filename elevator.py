import time

ELEVATOR_FLOORS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11,
                   "12": 12, "13": 13, "R": 14}

class Elevator:

    def __init__(self, side):

        self.side = side
        self.door_state = "closed"
        self.location = 1
        self.destination_floor = None
        self.moving = False
        self.call_direction = None

    def initial_display(self, action):
        print(f"on the way to {action} human on floor {self.destination_floor}")

    def arrival(self):

        print(f"{self.destination_floor}")
        self.location = self.destination_floor
        self.open_door()
        self.close_door()

    def open_door(self):
        self.door_state = "opened"
        time.sleep(1)
        print(f"door {self.door_state}")

    def close_door(self):
        self.door_state = "closed"
        time.sleep(1)
        print(f"door {self.door_state}")

    def same_floor(self):
        self.open_door()
        print("Oops. Maybe it was a ghost.")
        self.close_door()
        pass

    def move_up(self):

        while self.destination_floor - 1 > self.location:
            time.sleep(1)
            self.location += 1
            self.call_direction = "down"
            print(f"{self.location}...")

    def move_down(self):

        while self.destination_floor + 1 > self.location:
            time.sleep(1)
            self.location -= 1
            self.call_direction = "down"
            print(f"{self.location}...")
        
    def move(self, action, destination, side):

        if self.side == side:
            self.destination_floor = destination

            if self.destination_floor == self.location:
                self.same_floor()

            elif action == "pick up":
                print(f"{self.side} elevator chosen")

                if self.destination_floor != self.location:
                    self.moving = True

                if self.destination_floor > self.location:
                    self.initial_display(action)
                    self.move_up()

                elif self.destination_floor < self.location:
                    self.initial_display(action)
                    self.move_down()
                self.arrival()
            
            elif action == "drop off":
                print(f"on the way to {self.destination_floor}")

                if self.destination_floor > self.location:
                    self.initial_display(action)
                    self.move_up()

                elif self.destination_floor < self.location:
                    self.initial_display(action)
                    self.move_down()
                self.arrival()
                