class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:.2f})"

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def summary(self) -> str:
        return f"{self.owner}'s balance is N{self.balance:.2f}"

    def is_overdrawn(self) -> bool:
        return self.balance < 0

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds :)")
        
        self.balance -= amount
        return self.balance

accounts = [
    BankAccount("Adamu", 5000.0),
    BankAccount("Joy", 7500.9),
    BankAccount("David", 5800.8),
    BankAccount("Lucy", 4990.3)    
]

VIPs = [vips.owner for vips in accounts if vips.balance > 5000]
print(VIPs)

balance_map = {owner.owner: owner.balance for owner in accounts}

print(balance_map)
for account in accounts:
    try :
    
        account.deposit(2500.5)
        account.withdraw(10995.4)
        print(account.summary())
        print(account.is_overdrawn())
    except InsufficientFundsError as error:
        print(f"There is an error {error}")


