class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        account = Account(account_holder, initial_balance)
        self.accounts[account_holder] = account
        print(f"Account created for {account_holder}.")

    def close_account(self, account_holder):
        if account_holder in self.accounts:
            del self.accounts[account_holder]
            print(f"Account for {account_holder} closed.")
        else:
            print(f"Account for {account_holder} not found.")

    def display_account_info(self, account_holder):
        if account_holder in self.accounts:
            account = self.accounts[account_holder]
            account.check_balance()
        else:
            print(f"Account for {account_holder} not found.")



bank_system = BankSystem()

bank_system.create_account("John Doe", 1000)
bank_system.display_account_info("John Doe")
bank_system.accounts["John Doe"].withdraw(500)
bank_system.accounts["John Doe"].deposit(1500)
