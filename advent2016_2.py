#!/usr/bin/env python
# http://adventofcode.com/2016
from itertools import cycle
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


number_pad = {
    (-1, 1): "1",
    (0, 1): "2",
    (1, 1): "3",
    (-1, 0): "4",
    (0, 0): "5",
    (1, 0): "6",
    (-1, -1): "7",
    (0, -1): "8",
    (1, -1): "9"}

number_pad2 = {
    (0, 2): "1",
    (-1, 1): "2",
    (0, 1): "3",
    (1, 1): "4",
    (-2, 0): "5",
    (-1, 0): "6",
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, -1): "A",
    (0, -1): "B",
    (1, -1): "C",
    (0, -2): "D"}

number_pad_reversed2 = {k: v for v, k in number_pad.items()}


def process_move2(xstart, ystart, direction):
    x, y = xstart, ystart

    if direction == 'U':
        if y < 2 and x == 0:
            y += 1
        elif y < 1 and x in (-1, 1):
            y += 1
    elif direction == 'D':
        if y > -2 and x == 0:
            y -= 1
        elif y > -1 and x in (-1, 1):
            y -= 1
    elif direction == 'R':
        if x < 2 and y == 0:
            x += 1
        elif x < 1 and y in (-1, 1):
            x += 1
    elif direction == 'L':
        if x > -2 and y == 0:
            x -= 1
        elif x > -1 and y in (-1, 1):
            x -= 1

    return x, y, number_pad2[(x, y)]


def process_move(xstart, ystart, direction):
    x, y = xstart, ystart

    if direction == 'U':
        if y < 1:
            y += 1
    elif direction == 'D':
        if y > -1:
            y -= 1
    elif direction == 'R':
        if x < 1:
            x += 1
    elif direction == 'L':
        if x > -1:
            x -= 1
        
    return x, y, number_pad[(x, y)]



if __name__ == '__main__':
    x, y = -2, 0
    num = ''
    with open('advent2016-2_input.txt') as file:
        for line in file:
            for character in line:
                x, y, num = process_move2(x, y, character)
            log.debug('{}'.format(num))
