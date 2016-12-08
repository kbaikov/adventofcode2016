import pytest

from advent2016_7 import supports_tls


@pytest.mark.parametrize("string, expected", [
    ("abba[mnop]qrst", True),
    ("abcd[bddb]xyyx", False),
    ("aaaa[qwer]tyui", False),
    ("ioxxoj[asdfgh]zxcvbn", True),
])
def test_supports_tls(string, expected):
    assert supports_tls(string) == expected
