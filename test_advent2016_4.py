import pytest

from advent2016_4 import is_real_room


@pytest.mark.parametrize("room_string, checksum, expected", [
    ("aaaaa-bbb-z-y-x", "abxyz", True),
    ("a-b-c-d-e-f-g-h", "abcde", True),
    ("not-a-real-room", "oarel", True),
    ("totally-real-room", "decoy", False),
])
def test_is_real_room(room_string, checksum, expected):
    assert is_real_room(room_string, checksum) == expected
