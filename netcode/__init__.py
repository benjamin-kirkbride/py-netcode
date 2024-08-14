"""Netcode implementation in Python."""

# TODO: add more descriptive docstring.

MAC_BYTES: int = 16
CONNECTION_TIMEOUT_SEC: int = 15
PACKET_SEND_RATE_SEC: float = 1.0 / 10.0

# The size of a private key in bytes.
PRIVATE_KEY_BYTES: int = 32
# The size of the user data in a connect token in bytes.
USER_DATA_BYTES: int = 256
# The size of the connect token in bytes.
CONNECT_TOKEN_BYTES: int = 2048
# The maximum size of a packet in bytes.
MAX_PACKET_SIZE: int = 1200
# The version of the netcode protocol implemented by this crate.
NETCODE_VERSION: bytes = b"NETCODE 1.02\0"
