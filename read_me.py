"""
OVERALL PLAN:

ACTIONS

movement:
-initial position of the elevators is floor 1, not moving
-2 elevators that go up and down based on what floor the request is coming from and where it wants to go
-if the 2 elevators are equally near to a request, one elevator has priority
-elevators should pick up multiple requests, and only react to ones that are in the same direction AND not too sudden


speed:
-speed should be at least triple or more the speed of a real elevator


PHYSICAL THINGS

elevator system:
-2 elevators

indidivual elevator:
-1 door
-inside has button panel
-can hold maximum of certain amount of people

floors:
-14 floors

buttons: outside on each floor:
-floor 1 has "up" button, floor 2-13 have 'up' and 'down' buttons, top floor 'R' has 'down' button
-multiple calls for the elevator happen, and are queued 


buttons: inside the elevators:
-buttons 1-13 and R can be pressed and kept on, and are queued for each elevator
-'open' and 'close' buttons can be utilized when elevator is stopped
-'alarm' button can used in emergency to call a phone number for help

passengers:
-can appear outside on floor 1-14
-have the ability to press 'up' or 'down' button from outside
-have the ability to press any panel button from inside

display:
-shows the display inside each of the elevators
-shows the current floor and direction



USER EXPERIENCE

elevator god
-can choose how many people and where they appear, then either choose where they go or leave it to random

elevator game
-play as one person and go to different floors and experience something new or a challenge at each floor



"""