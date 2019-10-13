import random
import math

waypoints = None

waypoint = [
    (12, 40),
    (46, 87),
    (54, 23),
    (51, 34),
    (34, 24),
    (21, 49),
    (64, 45),
    (45, 25),
    (15, 41),
    (63, 32)
]

def __init__(self, waypoints):
    self.waypoints = waypoints

def shortestPath(waypoints):
    length = len(waypoints)
    iterations = 100000
    count = 0
    while count < iterations:
        a = random.sample(range(1,length-1), 2)
        if(a[0] == a[1]-1):
            a[0] -= 1
            a[1] += 1
        elif a[0] == a[1]-2:
            a[0] -= 1
        if isCrossing(waypoints[a[0]], waypoints[a[0]+1], waypoints[a[1]], waypoints[a[1]-1]):
            waypoints = swapPosition(waypoints, a[0], a[1])
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

def takeBestResult():
    lowest = shortestPath(waypoint)
    #lowestWaypoints = shortestPath(waypoint).waypoints
    for x in range(0,5):
        current = shortestPath(waypoint)
        #currentWaypoints = shortestPath(waypoint).waypoints
        if(current < lowest):
            lowest = current
            #lowestWaypoints = currentWaypoints
    
    #print(lowestWaypoints)

    return lowest

print(takeBestResult())

