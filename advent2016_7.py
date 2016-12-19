#!/usr/bin/env python
# http://adventofcode.com/2016

import re
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def supports_tls(s):
    if has_abba(s)[0]:
        if not abba_inside_square_brackets(s, has_abba(s)[1]):
            return True
    return False


def supports_ssl(s):
    in_square = re.findall(r'\[(.*?)\]', s)
    for sample in in_square:
        has, bab = has_bab(sample)
        if has:
            outside_square = re.findall(r"(.*?)(?:\[.*?\]|$)", s)
            antibab = bab[1] + bab[0] + bab[1]
            for sample in outside_square:
                if antibab in sample:
                    return True
            return False


def has_bab(s, pattern=None):
    if pattern:
        if pattern in s:
            return True, pattern
        else:
            return False, None
    index = 0
    while index + 2 < len(s):
        if s[index] == s[index + 1]:
            index += 1
            continue
        if s[index] == s[index + 2] and s[index] != s[index + 1]:
            return True, s[index:index+3]
        index += 1
    return False, None


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


def bab_inside_square_brackets(s, bab):
    antipattern = bab[1] + bab[0] + bab[1]
    in_square = re.findall(r'\[(.*?)\]', s)
    for sample in in_square:
        if has_bab(sample, pattern=antipattern)[0]:
            return True
    return False


def abba_inside_square_brackets(s, abba):
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
            results.append(supports_ssl(line))
        print(results.count(True))


