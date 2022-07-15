"""
implement two vechicle classes:

Car:
- the constructor for Car must take two arguments. The first of 
them is its maximum speed, and the second one is a string that
denotes the units in which the speed is given: either "km/h" or 
"mph"

- The class must be implemented to return a string based on the
arguments. For example, if car is an object of class Car with a 
maximum speed of 120, and the unit is "km/h", then printing car
prints the following string: "Car with the maximum speed of 
120 km/h", without quotes

Boat:
- the constructor for Boat must take a single argument denoting
its maximum speed in knots

- the class must be implemented to return a string based on the
argument. For example, if boat is an object of class Boat with
a maximum speed of 82, the printing boat print the following 
string: "Boat with the maximum speed of 82 knots", without the quotes

"""

import math
import os
import random
import re
import sys
from turtle import speed

class Car:
    def __init__(self,speed,dist):
        self.speed = speed
        self.dist = dist

    def __str__(self):
        return f"Car with the maximum speed of {self.speed} {self.dist}"

class Boat:
    def __init__(self,speed):
        self.speed = speed
    
    def __str__(self):
        return f"Boat with the maximum speed of {self.speed} knots"

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    q = int(input())
#    queries = []
#    for _ in range(q):
#        args = input().split()
#        vehicle_type, params = args[0], args[1:]
#        if vehicle_type == "car":
#            max_speed, speed_unit = int(params[0]), params[1]
#            vehicle = Car(max_speed, speed_unit)
#        elif vehicle_type == "boat":
#            max_speed = int(params[0])
#            vehicle = Boat(max_speed)
#        else:
#            raise ValueError("invalid vehicle type")
#        fptr.write("%s\n" % vehicle)
#    fptr.close()

    car = Car(151, "km/h")
    print(car)
    boat = Boat(77)
    print(boat)
    car2 = Car(251, "mph")
    boat2 = Boat(101)
    print(car2)
    print(boat2)
