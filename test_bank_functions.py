import pytest

from d1 import InsufficientFundsError, BankAccount

def test_deposit_increases_balance() -> None:
    account = BankAccount("Rapheal", 1000.0)
    account.deposit(500.0)
    assert account.balance == 1500.0