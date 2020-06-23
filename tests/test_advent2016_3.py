import pytest

from advent2016_3 import triangle


@pytest.mark.parametrize("a, b, c, expected", [(3, 3, 3, True), (5, 10, 25, False)])
def test_triangle(a, b, c, expected):
    assert triangle(a, b, c) == expected
