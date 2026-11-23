class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def summary(self) -> str:
        return f"{self.owner}'s balance is N{self.balance:.2f}"

    def isOverDrawn(self) -> bool:
        return self.balance < 0

account = BankAccount("Adamu", 5000.0)
account.deposit(2500.5)
print(account.summary())
print(account.isOverDrawn())


