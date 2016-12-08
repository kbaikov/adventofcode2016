#!/usr/bin/env python
# http://adventofcode.com/2016

from collections import Counter
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def supports_tls(string):
    pass

if __name__ == '__main__':
    with open('advent2016-7_input.txt') as file:
        letters = [[] for _ in range(8)]
        for line in file:
            line = line.rstrip('\r\n')
            
