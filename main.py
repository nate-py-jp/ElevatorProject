from human import Human
from elevator import Elevator
from dual_brain import DualBrain

print("Starting main...")

# create human, elevators and brain
nate = Human()
elevator_right = Elevator("right")
elevator_left = Elevator("left")
dual_brain = DualBrain()

while True:

    # set human's starting floor
    nate.set_starting_floor()

    # choose right or left elevator
    dual_brain.choose_side(nate.location, elevator_right.location, elevator_left.location)

    # move elevator to destination floor
    elevator_right.move(nate.action, nate.location, dual_brain.priority_elevator)
    elevator_left.move(nate.action, nate.location, dual_brain.priority_elevator)

    # set the human's destination floor
    nate.set_destination_floor()

    dual_brain.choose_side(nate.location, elevator_right.location, elevator_left.location)

    # move elevator to destination floor
    elevator_right.move(nate.action, nate.destination, dual_brain.priority_elevator)
    elevator_left.move(nate.action, nate.destination, dual_brain.priority_elevator)

    # print location of both elevators after full trip
    print(elevator_right.location, elevator_left.location)

