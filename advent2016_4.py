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
    c = Counter(room_string).most_common(5)
    least_value = c[-1][1]
    # sort reversed on the value and then by the key
    sorted_c = sorted(c, key=lambda x: (-x[1], x[0]))
    most_common_string = ''.join([elem[0] for elem in sorted_c])
    log.debug('{} {} {}'.format(room_string, checksum, most_common_string))
    if most_common_string == checksum:
        return True
    else:
        return False


if __name__ == '__main__':
    with open('advent2016-4_input.txt') as file:
        for line in file:
            line = line.rstrip('\r\n')
            room_string, sector_id, checksum = partition_string(line)
            log.debug('{} {}'.format(line, is_real_room(room_string, checksum)))
            
