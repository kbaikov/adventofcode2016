#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import deque
import re


def unzipped(s):
    stack = deque()
    pattern = re.compile(r"\((\d+)x(\d+)\)")  # digits x digits in brackets
    current_position = 0
    while True:
        marker = pattern.search(s, current_position)
        if not marker:
            stack.append(s[current_position:])
            break
        start, end = marker.span()
        length, _, multiplier = marker.group().strip("()").partition("x")
        length = int(length)
        multiplier = int(multiplier)
        stack.append(s[current_position:start])
        stack.append(s[end : end + length] * multiplier)
        current_position = end + length
    return "".join(stack)


if __name__ == "__main__":

    with open("advent2016-9_input.txt") as file:
        print(len(unzipped(file.read().strip())))  # 107035
