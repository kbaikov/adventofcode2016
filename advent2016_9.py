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
        length, multiplier = int(marker.group(1)), int(marker.group(2))
        stack.append(s[current_position:start])
        stack.append(s[end : end + length] * multiplier)
        current_position = end + length
    return "".join(stack)


def unzipped2(s):
    """from https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/daz2o0d/"""
    marker = re.search(r"\((\d+)x(\d+)\)", s)
    if not marker:
        return len(s)

    current_position = marker.start(0)
    length, multiplier = int(marker.group(1)), int(marker.group(2))

    i = current_position + len(marker.group())
    return (
        len(s[:current_position])
        + unzipped2(s[i : i + length]) * multiplier
        + unzipped2(s[i + length :])
    )


if __name__ == "__main__":
    with open("advent2016-9_input.txt") as file:
        text = file.read().strip()
        print(len(unzipped(text)))  # 107035
        print(unzipped2(text))  # 11451628995
