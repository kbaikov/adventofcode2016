#!/usr/bin/env python
# http://adventofcode.com/2016
from itertools import islice
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def is_real_room(room_string, checksum):
    pass


if __name__ == '__main__':
    z = []
    with open('advent2016-4_input.txt') as file:
        lines = []
        for line in file:
            lines.append(line.split())
            if len(lines) == 3:
                z.append(triangle(lines[0][0], lines[1][0], lines[2][0]))
                z.append(triangle(lines[0][1], lines[1][1], lines[2][1]))
                z.append(triangle(lines[0][2], lines[1][2], lines[2][2]))
                lines = []
            log.debug('{}'.format(z.count(True)))
