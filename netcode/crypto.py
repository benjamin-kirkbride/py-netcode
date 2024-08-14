import secrets

from netcode import PRIVATE_KEY_BYTES


class Key(bytes):
    """A key for encrypting/decrypting packets and connect tokens."""

    def __new__(cls, value: bytes) -> "Key":
        """New."""
        if len(value) != PRIVATE_KEY_BYTES:
            msg = f"Key must be {PRIVATE_KEY_BYTES} bytes"
            raise ValueError(msg)

        return super().__new__(cls, value)


def generate_key() -> Key:
    """Generate a new key."""
    return Key(secrets.token_bytes(PRIVATE_KEY_BYTES))
