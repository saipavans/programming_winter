import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_between_points(self, other_point):
        x_distance = abs(self.x - other_point.x)
        y_distance = abs(self.y - other_point.y)
        distance = math.pow(((x_distance ** 2 + y_distance ** 2)), 0.5)
        return distance

    def __add__(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        return Point(new_x, new_y)


def main():
    origin = Point(0, 0)
    point1 = Point(1, 1)
    print("Distance between origin and (1,1):", origin.distance_between_points(point1))
    new_point = origin + point1
    print("New point:", new_point.x, new_point.y)


if __name__ == '__main__':
    main()
