import math


def euclidDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def circlesIsOverlapCheck(c1, c2):
    r1, r2 = c1.radius, c2.radius
    dist = euclidDistance(c1.pos, c2.pos)
    return r1 + r2 > dist
