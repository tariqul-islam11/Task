class BankAccount:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float):
        self.account_numnber = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The deposit amount must be positive")
        self.balance += amount
        print("Tk.", amount, "was  depositted.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The Withdraw amount must be positive")
        self.balance -= amount
        print("TK.", amount, "was withdrawn.")
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return(f"Account Number: {self.account_numnber}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Current Balance: TK. {self.balance:.2f}")
    
acc1 = BankAccount("123", "Tarek", 10000.0)
print(acc1)
acc1.deposit(2000)
acc1.withdraw(7000)
print(acc1)