class InsufficientFundsError(Exception):
    pass


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

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds :)")
        
        self.balance -= amount
        return self.balance

account = BankAccount("Adamu", 5000.0)
account.deposit(2500.5)
try :
    account.withdraw(10994.4)
except InsufficientFundsError as error:
    print(f"There is an error{error}")

print(account.summary())
print(account.isOverDrawn())

