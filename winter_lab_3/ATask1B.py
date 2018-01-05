from winter_lab_3 import ATask1A as t1
import math


def display_chi_square(a, b):
    for i in range(a, b):
        square_root_standard = float(math.sqrt(i))
        square_root_custom = float(t1.square_root(i))
        difference = abs(square_root_standard - square_root_custom)
        print("%-5i%-20e%-20e%-20e" %(i, square_root_standard, square_root_custom, difference))

display_chi_square(1,9)