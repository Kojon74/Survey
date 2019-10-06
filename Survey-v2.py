import random
import math

waypoints = None

waypoint = [
    (12, 45),
    (46, 87),
    (54, 2523),
    (51, 864),
    (34, 324),
    (12, 45),
    (46, 87),
    (54, 2523),
    (51, 864),
    (36, 243)
]

def __init__(self, waypoints):
    self.waypoints = waypoints

def shortestPath(waypoints):
    iterations = 2000000
    count = 0
    length = len(waypoints)
    while count < iterations:
        a1 = random.randint(0, length - 1)
        a2 = random.randint(0, length - 2)
        b1 = random.randint(0, length - 3)
        b2 = random.randint(0, length - 4)
        if a1 <= a2:
            a2 += 1
        elif a1 <= b1 & a2 <= b1:
            b1 += 2
        elif a1 <= b1 | a2 <= b1:
            b1 += 1
        elif a1 <= b2 & a2 <= b2 & b1 <= b2:
            b2 += 3
        elif (a1 <= b2 & a2 <= b2) | (a1 <= b2 & b1 <= b2) | (a2 <= b2 & b1 <= b2):
            b2 += 2
        elif a1 <= b2 | a2 <= b2 | b1 <= b2:
            b2 += 1
        if isCrossing(waypoints[a1], waypoints[a2], waypoints[b1], waypoints[b2]):
            waypoints = swapPosition(waypoints, a2, b2)
        count += 1
    distance = totalDistance(waypoints)
    return distance

def isCrossing(pointA1, pointA2, pointB1, pointB2):
    if orientation(pointA1, pointA2, pointB1) == orientation(pointA1, pointA2, pointB2):
        return False
    return True

# Determines orientation of 3 points going from p --> q --> r
# 0 - Colinear (Doesn't take colinear into account since very unlikely)
# 1 - Clockwise
# 2 - Anti-clockwise
def orientation(p, q, r):
    value = (q[1] - p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])
    return 1 if (value > 0) else 2

def swapPosition(_waypoints, pos1, pos2):
    _waypoints[pos1], _waypoints[pos2] = _waypoints[pos2], _waypoints[pos1]
    return _waypoints

def totalDistance(_waypoints):
    length = len(_waypoints)
    a = 0
    distance = 0
    while a < length - 1:
        distance += notTotalDistance(_waypoints[a], _waypoints[a+1])
        a += 1
    return distance

def notTotalDistance(start, end):
    return math.sqrt((start[1]-end[1])**2 + (start[0] - end[0])**2)

print(shortestPath(waypoint))

