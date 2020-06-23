import pytest

from advent2016_2 import process_move


@pytest.mark.parametrize(
    "xstart, ystart, direction, expected",
    [
        (0, 0, "U", (0, 1, "2")),
        (0, 0, "D", (0, -1, "8")),
        (0, 0, "L", (-1, 0, "4")),
        (0, 0, "R", (1, 0, "6")),
    ],
)
def test_process_move(xstart, ystart, direction, expected):
    assert process_move(xstart, ystart, direction) == expected
