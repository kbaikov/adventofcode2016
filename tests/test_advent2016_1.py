import pytest

from advent2016_1 import location


@pytest.mark.parametrize(
    "xstart, ystart, turn, distance, current_direction, expected",
    [
        (0, 0, "L", 3, "N", (-3, 0, "W")),
        (0, 0, "R", 3, "N", (3, 0, "E")),
        (0, 0, "L", 3, "E", (0, 3, "N")),
        (0, 0, "R", 3, "S", (-3, 0, "W")),
    ],
)
def test_location(xstart, ystart, turn, distance, current_direction, expected):
    assert location(xstart, ystart, turn, distance, current_direction) == expected
