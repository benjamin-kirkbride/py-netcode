import pydantic

from netcode import crypto
from netcode.types import Address, ClientID, Sequence


class Connection(pydantic.BaseModel):
    confirmed: bool
    connected: bool
    client_id: ClientID
    addr: Address
    timeout: float
    last_access_time: float
    last_send_time: float
    last_receive_time: float
    send_key: crypto.Key
    receive_key: crypto.Key
    sequence: Sequence
