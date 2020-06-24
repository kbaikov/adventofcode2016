import pytest

from advent2016_9 import *


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ADVENT", "ADVENT"),
        ("A(1x5)BC", "ABBBBBC"),
        ("(3x3)XYZ", "XYZXYZXYZ"),
        ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
        ("(6x1)(1x3)A", "(1x3)A"),
        ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
    ],
)
def test_unzipped(string, expected):
    assert unzipped(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
)
def test_unzipped2(string, expected):
    assert unzipped2(string) == expected
