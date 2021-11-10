
class Point:

        def __init__(self, x, y):
            self.x = int(x)
            self.y = int(y)

        def dist(self, other):
            if isinstance(other, Point):
                return((self.x-other.x) ** 2 + (self.y-other.y) ** 2) ** 0.5
            else:
                raise ValueError("Object is not a point")
try:
    point1 = Point(3,5)
    point2 = Point(2,4)
    point3 = 3

    print(Point.dist(point1, point2))
except ValueError:
    print("Object is not a point")
except TypeError:
    print("Missing args")

