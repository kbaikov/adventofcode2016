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


if __name__ == '__main__':
    print(find_pass('cxdnnyjw'))
