#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import deque
import logging as log
from pprint import pprint
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s')


def unzipped(s):
    pass

if __name__ == '__main__':
    with open('advent2016-9_input.txt') as file:
        for line in file:
            line = line.rstrip('\r\n')
            print(unzipped('A(1x5)BC'))

