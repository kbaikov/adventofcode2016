#!/usr/bin/env python
# http://adventofcode.com/2016

import hashlib
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def find_pass(input):
    i = 0
    password = ''
    while len(password) < 8:
        input = '{}{}'.format(input[:8], i)
        input_b = input.encode()
        m = hashlib.md5(input_b)
        h = m.hexdigest()
        if h[:5] == '00000':
            password += h[5]
            i += 1
        else:
            i += 1
            continue
    return password


def find_pass_with_position(input):
    l = len(input)
    i = 0
    password = [None for x in range(8)]
    while not all(password):
        input = '{}{}'.format(input[:l], i)
        input_b = input.encode()
        m = hashlib.md5(input_b)
        h = m.hexdigest()
        if h[:5] == '00000':
            position = h[5]
            character = h[6]
            try:
                if password[int(position)] == None: 
                    password[int(position)] = character
            except (IndexError, ValueError):
                pass
        i += 1
    return ''.join(password)


if __name__ == '__main__':
    print(find_pass_with_position('cxdnnyjw'))
