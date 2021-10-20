import math

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    def __copy__(self):
        return Point(self.x, self.y)


class Tri:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        p = 0
        p += math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        p += math.sqrt((b.x - c.x) ** 2 + (b.y - c.y) ** 2)
        p += math.sqrt((c.x - a.x) ** 2 + (c.y - a.y) ** 2)
        return p
    def area(self):
    def contains(self, point):

point = Point(3,7)

print(point.x)
