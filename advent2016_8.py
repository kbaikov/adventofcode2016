#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import deque
import logging as log
from pprint import pprint
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s')


grid = {(c, r): '.' for c in range(50) for r in range(6)}


def rect(x, y):
    for ix in range(x):
        for iy in range(y):
            grid[ix, iy] = 'x'


def rotate_column(column, rotation):
    d = deque([grid[column, y] for y in range(6)])
    d.rotate(rotation)
    for i, x in enumerate(d):
        grid[column, i] = x


def rotate_row(row, rotation):
    d = deque([grid[x, row] for x in range(50)])
    d.rotate(rotation)
    for i, x in enumerate(d):
        grid[i, row] = x


def print_grid():
    for y in range(6):
        for x in range(50):
            print(grid[x, y], end=' ')
        print()


def parse_commands(line):
    function = None
    parameter1 = None
    parameter2 = None
    if line.startswith("rect"):
        function = 'rect'
        parameter1, _, parameter2 = line.rpartition('x')
    elif line.startswith("rotate row"):
        function = 'rotate_row'
        parameter1, _, parameter2 = line.rpartition(' by ')
    else:
        function = 'rotate_column'
        parameter1, _, parameter2 = line.rpartition(' by ')

    if parameter1[-2:].isdigit():
        parameter1 = parameter1[-2:]
    else:
        parameter1 = parameter1[-1]
    return function, parameter1, parameter2

if __name__ == '__main__':
    # parse_commands('rotate row y=0 by 5')
    # rect(3, 2)
    # print_grid()
    # rotate_column(1, 1)
    # print_grid()
    # rotate_row(0, 4)
    # print_grid()
    # rotate_column(1, 1)
    # print_grid()
    # log.debug(grid[0, 0])
    with open('advent2016-8_input.txt') as file:
        letters = [[] for _ in range(8)]
        for line in file:
            line = line.rstrip('\r\n')
            f, p1, p2 = parse_commands(line)
            locals()[f](int(p1), int(p2))
    print_grid()
    print(list(grid.values()).count('x'))

