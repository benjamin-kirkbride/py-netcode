import pytest

from netcode import util


@pytest.mark.parametrize(
    ("bits", "expected"),
    [
        (8, 255),
        (16, 65535),
        (32, 4294967295),
        (64, 18446744073709551615),
    ],
)
def test_max_unsigned_value(bits, expected):
    assert util.max_unsigned_value(bits) == expected
