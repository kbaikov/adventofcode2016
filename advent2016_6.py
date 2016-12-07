#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import Counter
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



if __name__ == '__main__':
    with open('advent2016-6_input.txt') as file:
        sector_sum = 0
        for line in file:
            line = line.rstrip('\r\n')
    print()
