#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import Counter
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def supports_tls(s):
    if has_abba(s)[0]:
        if not abba_inside_square_brackets(s, has_abba(s)[1]):
            return True
    return False


def has_abba(s):
    index = 0
    while index + 3 < len(s):
        if s[index] == s[index + 1]:
            index += 1
            continue
        if s[index] == s[index + 3] and s[index + 1] == s[index + 2]:
            return True, s[index:index+4]
        index += 1
    return False, None


def abba_inside_square_brackets(s, abba):
    import re
    in_square = re.findall(r'\[(.*?)\]', s)
    for sample in in_square:
        if has_abba(sample)[0]:
            return True
    return False


if __name__ == '__main__':
    results = []
    with open('advent2016-7_input.txt') as file:
        for line in file:
            line = line.rstrip('\r\n')
            results.append(supports_tls(line))
        print(results.count(True))


