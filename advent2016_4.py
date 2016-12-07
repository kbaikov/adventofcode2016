#!/usr/bin/env python
# http://adventofcode.com/2016
import re
from collections import Counter
import logging as log
import operator
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def partition_string(s):
    # match = re.search(r'(?P<room_string>\.+)(?P<sector_id>[0-9])(?P<checksum>\[[a-z]\])', s)
    room_string = s[:-11].replace('-', '')
    sector_id = s[-10: -7]
    checksum = s[-6: -1]
    return room_string, sector_id, checksum


def is_real_room(room_string, checksum):
    c = Counter(room_string).most_common(100)
    # sort reversed on the value and then by the key
    sorted_c = sorted(c, key=lambda x: (-x[1], x[0]))
    most_common_string = ''.join([elem[0] for elem in sorted_c])
    if most_common_string[:5] == checksum:
        return True
    else:
        return False


def sector_sum():
    with open('advent2016-4_input.txt') as file:
        sector_sum = 0
        for line in file:
            line = line.rstrip('\r\n')
            room_string, sector_id, checksum = partition_string(line)
            if is_real_room(room_string, checksum):
                sector_sum += int(sector_id)
    return sector_sum

if __name__ == '__main__':
    print(sector_sum)
