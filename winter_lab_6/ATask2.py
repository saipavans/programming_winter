import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_between_points(self, another_point):
        x_diff = abs(self.x - another_point.x)
        y_diff = abs(self.y - another_point.y)
        return math.pow(x_diff ** 2 + y_diff ** 2, 0.5)


class Rectange:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def find_center(self):
        return Point(self.corner.x + self.width / 2, self.corner.y + self.height / 2)

    def move_rectange(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def move_rectangle_new(self, dx, dy):
        new_corner = Point(self.corner.x + dx, self.corner.y + dy)
        return Rectange(self.height, self.width, new_corner)


def main():

    origin = Point(0, 0)

    rectangle = Rectange(1, 1, origin)
    center = rectangle.find_center()
    print("Center of Rectange", center.x, center.y)

    rectangle.move_rectange(1, 1)
    center = rectangle.find_center()
    print("Moved rectange center", center.x, center.y)

    new_moved_rectange = rectangle.move_rectangle_new(1,1)
    print("The new rectangle created while moving has its center at: ", new_moved_rectange.find_center().x, new_moved_rectange.find_center().y)


if __name__ == '__main__':
    main()
