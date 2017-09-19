import math

DEG_TO_RAD = 0.0174533
RAD_TO_DEG = 57.2958

# Returns distnace between two points
def pointDistance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Returns angle between two points in radians
def pointAngle(x1,y1,x2,y2):
    return math.atan2(y2-y1, x2-x1)

# Returns value within a range [_min, _max]. _min and _max are both inclusive.
def clamp(value, _min, _max): return max(_min, min(_max, value))
