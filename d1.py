from dataclasses import dataclass
from decimal import Decimal


class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

@dataclass
class BankAccount:
    owner: str
    balance: Decimal = Decimal("0.00")

    def deposit(self, amount: Decimal) -> Decimal:
        if amount <= Decimal("0"):
            raise InvalidAmountError(f"Cannot deposit amount {amount:.2f} it is unallowed")
        self.balance += amount
        return self.balance

    def summary(self) -> str:
        return f"{self.owner}'s balance is N{self.balance:.2f}"

    def is_overdrawn(self) -> bool:
        return self.balance < Decimal("0")

    def withdraw(self, amount: Decimal) -> Decimal:
        if amount <= Decimal("0"):
            raise InvalidAmountError(f"Cannot withdraw amount {amount:.2f} it is unallowed")
        
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw N{amount:.2f}; balance is N{self.balance:.2f}")
        
        self.balance -= amount
        return self.balance

if __name__ == "__main__":
    accounts = [
        BankAccount("Adamu", 5000.0),
        BankAccount("Joy", 7500.9),
        BankAccount("David", 5800.8),
        BankAccount("Lucy", 4990.3)    
    ]

    vips = [vip.owner for vip in accounts if vip.balance > 5000]
    print(vips)

    balance_map = {owner.owner: owner.balance for owner in accounts}

    print(balance_map)
    for account in accounts:
        try :
        
            account.deposit(2500.5)
            account.withdraw(8000.4)
            print(account.summary())
            print(account.is_overdrawn())
        except (InsufficientFundsError, InvalidAmountError) as error:
            print(f"There is an error: {error}")

        try:
            account.deposit(-780.0)
        except (InvalidAmountError) as error:
            print(f"There is an error: {error}")