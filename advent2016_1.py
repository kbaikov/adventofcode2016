#!/usr/bin/env python
# http://adventofcode.com/2016
from itertools import cycle
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


directions = ("N", "E", "S", "W")


def location(xstart, ystart, turn, distance, current_direction):
    x, y = xstart, ystart
    c = cycle(directions)
    cur = next(c)
    while cur != current_direction:
        cur = next(c)

    if turn == "R":
        cur = next(c)
    elif turn == "L":
        for _ in range(3):
            cur = next(c)

    if cur == "N":
        y += distance
    elif cur == "S":
        y -= distance
    elif cur == "E":
        x += distance
    elif cur == "W":
        x -= distance

    return x, y, cur


def location2(xstart, ystart, turn, distance, current_direction, visited):
    x, y = xstart, ystart
    c = cycle(directions)
    cur = next(c)
    while cur != current_direction:
        cur = next(c)

    if turn == "R":
        cur = next(c)
    elif turn == "L":
        for _ in range(3):
            cur = next(c)

    if cur == "N":
        for _ in range(distance):
            y += 1
            if (x, y) in visited:
                print(x, y)
            visited.append((x, y))
    elif cur == "S":
        for _ in range(distance):
            y -= 1
            if (x, y) in visited:
                print(x, y)
            visited.append((x, y))
    elif cur == "E":
        for _ in range(distance):
            x += 1
            if (x, y) in visited:
                print(x, y)
            visited.append((x, y))
    elif cur == "W":
        for _ in range(distance):
            x -= 1
            if (x, y) in visited:
                print(x, y)
            visited.append((x, y))

    return x, y, cur, visited


def seen2(L):
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for item in L:
        if item in seen:
            seen2_add(item)
        else:
            seen_add(item)
    return seen2


if __name__ == "__main__":
    x, y, d = 0, 0, "N"
    visited = [(x, y)]
    with open("advent2016-1_input.txt") as file:
        for line in file:
            for entry in line.split(", "):
                x, y, d, visited = location2(
                    x, y, str(entry[0]), int(entry[1:]), d, visited
                )
                # log.debug('{} {} {} {}'.format(x, y, d, entry))
            # log.debug('{}'.format(visited))
            # print(seen2(visited))
