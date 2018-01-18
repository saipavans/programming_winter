import math
class Point:

    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y


def distance_between_points(self, another_point):
    x_diff = abs(self.x - another_point.x)
    y_diff = abs(self.y - another_point.y)
    return math.pow(x_diff**2 + y_diff**2,0.5)

def main():
    p1 = Point(0,0)
    p2 = Point(1,1)
    print(distance_between_points(p1,p2))

if __name__ == '__main__':
    main()