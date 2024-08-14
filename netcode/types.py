import pydantic

from netcode import util


class u64(int):  # noqa: N801
    """Unsigned 64-bit integer."""

    def __new__(cls, value: int) -> "u64":
        """New."""
        if value < 0:
            msg = "u64 must be non-negative"
            raise ValueError(msg)

        if value > util.max_unsigned_value(64):
            msg = f"u64 must be less than {util.max_unsigned_value(64)}"
            raise ValueError(msg)

        return super().__new__(cls, value)


class Sequence(u64):
    # TODO: explain what a sequence is/does
    # it's not as simple as it may seem
    # TODO: should this go in server.py?
    pass


class ClientID(u64):
    """The client id from a connect token.

    Must be unique for each client.
    """


class Address(pydantic.BaseModel):
    """Address of a network host."""

    host: str
    port: int
