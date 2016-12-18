import pytest

from advent2016_7 import supports_tls, has_abba, abba_inside_square_brackets


@pytest.mark.parametrize("string, expected", [
    ("abba[mnop]qrst", True),
    ("abcd[bddb]xyyx", False),
    ("aaaa[qwer]tyui", False),
    ("ioxxoj[asdfgh]zxcvbn", True),
])
def test_supports_tls(string, expected):
    assert supports_tls(string) == expected


@pytest.mark.parametrize("string, expected", [
    ("abba", (True, 'abba')),
    ("aaaa", (False, None)),
    ("aaba", (False, None)),
    ("ioxxoj", (True, 'oxxo')),
])
def test_has_abba(string, expected):
    assert has_abba(string) == expected


@pytest.mark.parametrize("string, match, expected", [
    ("[abba]", 'abba', True),
    ("[i]oxxoj", 'oxxo', False),
    ("ioxxo[j]", 'oxxo', False),
    ("[oxxo]", 'oxxo', True),
])
def test_abba_inside_square_brackets(string, match, expected):
    assert abba_inside_square_brackets(string, match) == expected
