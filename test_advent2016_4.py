import pytest

from advent2016_4 import caesar_cipher, is_real_room, partition_string


@pytest.mark.parametrize("raw_string, expected", [
    ("aaaaa-bbb-z-y-x-123[abxyz]", ("aaaaabbbzyx", "123", "abxyz"),),
    ("a-b-c-d-e-f-g-h-987[abcde]", ("abcdefgh", "987", "abcde")),
    ("not-a-real-room-404[oarel]", ("notarealroom", "404", "oarel")),
    ("totally-real-room-200[decoy]", ("totallyrealroom", "200", "decoy")),
])
def test_partition_string(raw_string, expected):
    assert partition_string(raw_string) == expected


@pytest.mark.parametrize("room_string, checksum, expected", [
    ("aaaaabbbzyx", "abxyz", True),
    ("abcdefgh", "abcde", True),
    ("notarealroom", "oarel", True),
    ("totallyrealroom", "decoy", False),
])
def test_is_real_room(room_string, checksum, expected):
    assert is_real_room(room_string, checksum) == expected


@pytest.mark.parametrize("raw_string, expected", [
    ("qzmt-zixmtkozy-ivhz-343[asdfg]", "very encrypted name")
])
def test_caesar_cipher(raw_string, expected):
    assert caesar_cipher(raw_string) == expected
