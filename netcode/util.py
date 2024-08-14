"""Utility functions for netcode."""


def max_unsigned_value(bits: int) -> int:
    """Return the maximum unsigned value for a given number of bits."""
    return (1 << bits) - 1
