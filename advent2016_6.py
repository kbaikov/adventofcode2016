#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import Counter
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


if __name__ == "__main__":
    with open("advent2016-6_input.txt") as file:
        letters = [[] for _ in range(8)]
        for line in file:
            line = line.rstrip("\r\n")
            for i, letter in enumerate(line):
                letters[i].append(letter)
        for char_list in letters:
            print("most common", Counter(char_list).most_common()[0])
            print("least common", Counter(char_list).most_common()[-1])
