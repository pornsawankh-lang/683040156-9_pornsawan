"""
Pornsawan Khareram
683040156-9
"""
class BankAccount:
    # Class attributes
    branch_name = "KKU Complex"
    branch_number = 1724
    last_saving_number = 0
    last_loan_number = 0

    def __init__(self, name, acc_type="saving", balance=0):
        if not name:
            raise ValueError("Name is required")

        self.name = name
        self.type = acc_type
        self.balance = balance

        if self.type == "saving":
            BankAccount.last_saving_number += 1
            self.acc_num = f"{BankAccount.branch_number}-1-{BankAccount.last_saving_number}"

        elif self.type == "loan":
            BankAccount.last_loan_number += 1
            self.acc_num = f"{BankAccount.branch_number}-2-{BankAccount.last_loan_number}"

        else:
            raise ValueError("Invalid account type")

    def get_balance(self):
        return self.balance

    def deposit(self, amount=0):
        self.balance += amount

    def withdraw(self, amount=0):
        self.balance -= amount

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Branch: {BankAccount.branch_name}")
        print(f"Name: {self.name}")
        print(f"Account number: {self.acc_num}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance}")
        print("----- End Record -----")
