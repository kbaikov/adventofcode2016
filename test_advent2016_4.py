import pytest

from advent2016_4 import is_real_room


@pytest.mark.parametrize("room_string, checksum, expected", [
    ("aaaaabbbzyx", "abxyz", True),
    ("abcdefgh", "abcde", True),
    ("notarealroom", "oarel", True),
    ("totallyrealroom", "decoy", False),
])
def test_is_real_room(room_string, checksum, expected):
    assert is_real_room(room_string, checksum) == expected
