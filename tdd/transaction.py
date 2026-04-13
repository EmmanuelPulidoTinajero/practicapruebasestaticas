from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    date: str
    amount: int
    balance: int