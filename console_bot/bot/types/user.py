from dataclasses import dataclass

USERS = {}


@dataclass
class User:
    name: str
    phone: int
