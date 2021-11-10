import raising as rs

def divide(a, b):
    return a/ b
class GeometryError:
    def __init__(self, description):
        self.description = description
    def __str__(self):
        return self.description

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist(self, other):
        if isinstance(other, Point):
            return((self.x-other.x) ** 2 + (self.y-other.y) ** 2) ** 0.5
        else:
            raise ValueError("Object is not a point")

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


point = Point(3,7)

print(point.x)
