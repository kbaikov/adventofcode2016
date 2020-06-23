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
