import pytest

from d1 import InsufficientFundsError, BankAccount

def test_deposit_increases_balance() -> None:
    account = BankAccount("Rapheal", 1000.0)
    account.deposit(500.0)
    assert account.balance == 1500.0

def test_withdraw_reduces_balance() -> None:
    account = BankAccount("Favour", 1000.0)
    account.withdraw(200.0)
    assert account.balance == 800.0

def test_overdraw_raises_insufficient_funds() -> None:
    account = BankAccount("Prince", 2000.0)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(2400.0)

def test_is_overdrown() -> None:
    account = BankAccount("Lucy", 100.0)
    assert account.is_overdrawn() is False

def test_is_overdrown2() -> None:
    account = BankAccount("Lucy", -50.0)
    assert account.is_overdrawn() is True