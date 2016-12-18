#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import deque
import logging as log
from pprint import pprint
log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s - %(levelname)s - %(message)s')


grid = {(c, r): None for c in range(7) for r in range(3)}


def rect(x, y):
    for ix in range(x):
        for iy in range(y):
            grid[ix, iy] = 'x'


def rotate_column(column, rotation):
    d = deque([grid[column, y] for y in range(3)])
    d.rotate(rotation)
    for i, x in enumerate(d):
        grid[column, i] = x


def rotate_row(row, rotation):
    d = deque([grid[x, row] for x in range(7)])
    d.rotate(rotation)
    for i, x in enumerate(d):
        grid[i, row] = x


def print_grid():
    for y in range(3):
        for x in range(7):
            print(grid[x, y], end='\t')
        print()


if __name__ == '__main__':
    rect(3, 2)
    print_grid()
    rotate_column(1, 1)
    print_grid()
    rotate_row(0, 4)
    print_grid()
    rotate_column(1, 1)
    print_grid()
    # log.debug(grid[0, 0])
    # with open('advent2016-8_input.txt') as file:
    #     letters = [[] for _ in range(8)]
    #     for line in file:
    #         line = line.rstrip('\r\n')
            
