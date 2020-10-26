from house import House
import sys
import os

ROWS, COLUMNS = os.popen('stty size', 'r').read().split()

house = House()
for i in range(500):
    if i == 10:
        house.set_begin_point(10)
        house.print_part()

    #  sys.stdout.write("a"),
    if (house.is_space_available(i)):
        sys.stdout.write("a"),
