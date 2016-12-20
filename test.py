import re


def to_aba(bab):
    return ''.join((''.join(bab[1:]), bab[1]))


def is_ssl(string):
    babs = re.findall(r'\[[^\]]*(\w)(\w)(\1).*?\]', string)
    abas = (to_aba(bab) for bab in babs)
    return any(re.search(r'%s\w*?(\[|$)' % aba, string) for aba in abas)


if __name__ == '__main__':
    results = []
    with open('advent2016-7_input.txt') as f:
        for line in f:
            line = line.rstrip('\r\n')
            results.append(is_ssl(line))
            print(is_ssl(line))
            print(results.count(True))
