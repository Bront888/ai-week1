import pytest

from d1 import InsufficientFundsError, BankAccount, LessThanZeroAmountError
@pytest.fixture
def account() -> BankAccount:
    return BankAccount("Rapheal", 1000.0)

@pytest.mark.parametrize(
        "deposit_amount, expected_balance",
        [
            (500.0, 1500),
            (4000.0, 5000)
        ]
)
def test_deposit_increases_balance(account: BankAccount, deposit_amount: float, expected_balance: float) -> None:
    account.deposit(deposit_amount)
    assert account.balance == expected_balance

def test_negative_deposit_is_rejected(account: BankAccount) -> None:
    with pytest.raises(LessThanZeroAmountError):
        account.deposit(-899.0)

def test_zero_deposit_is_rejected(account: BankAccount) -> None:
    with pytest.raises(LessThanZeroAmountError):
        account.deposit(0.0)

@pytest.mark.parametrize(
        "withdrawn_amount, expected_balance",
        [
            (300.0, 700.0),
            (1000.0, 0)
        ]
)
def test_withdraw_reduces_balance(account: BankAccount, withdrawn_amount: float, expected_balance: float) -> None:
    account.withdraw(withdrawn_amount)
    assert account.balance == expected_balance

def test_negative_withdraw_rejected(account: BankAccount) -> None:
    with pytest.raises(LessThanZeroAmountError):
        account.withdraw(-588.0)

def test_zero_withdraw_rejected(account: BankAccount) -> None:
    with pytest.raises(LessThanZeroAmountError):
        account.withdraw(0.0)

def test_overdraw_raises_insufficient_funds(account: BankAccount) -> None:
    with pytest.raises(InsufficientFundsError):
        account.withdraw(2400.0)

def test_is_overdrown_false_for_positive_balance() -> None:
    account = BankAccount("Lucy", 100.0)
    assert account.is_overdrawn() is False

def test_is_overdrown_true_for_negative_balance() -> None:
    account = BankAccount("Lucy", -50.0)
    assert account.is_overdrawn() is True