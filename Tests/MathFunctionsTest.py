from Math.MathFunctions import *

def pointTest():
    point1 = (0, 0)
    point2 = (2, 4)

    print("Point 1: {}".format(point1))
    print("Point 2: {}".format(point2))
    print("Point distance: {}".format(pointDistance(point1[0],point1[1],point2[0],point2[1])))
    angle = pointAngle(point1[0],point1[1],point2[0],point2[1]);
    print("Point angle: {:.3f}, {:.3f} degrees".format(angle, angle*RAD_TO_DEG))

pointTest()
