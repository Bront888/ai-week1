from dataclasses import dataclass


class InsufficientFundsError(Exception):
    pass

class LessThanZeroAmountError(Exception):
    pass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise LessThanZeroAmountError("Amount must be greater than zero")
        self.balance += amount
        return self.balance

    def summary(self) -> str:
        return f"{self.owner}'s balance is N{self.balance:.2f}"

    def is_overdrawn(self) -> bool:
        return self.balance < 0

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise LessThanZeroAmountError("Amount must be greater than Zero")
        
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw N{amount:.2f}; balance is N{self.balance:.2f}")
        
        self.balance -= amount
        return self.balance

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
if __name__ == "__main__":
    for account in accounts:
        try :
        
            account.deposit(2500.5)
            account.withdraw(8000.4)
            account.deposit(-780.0)
            print(account.summary())
            print(account.is_overdrawn())
        except (InsufficientFundsError, LessThanZeroAmountError) as error:
            print(f"There is an error {error}")


