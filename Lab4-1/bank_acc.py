"""
Pornsawan Khareram
683040156-9
"""
class BankAccount:
    # class variables
    branch_number = "001"
    saving_run = 0
    loaning_run = 0

    def __init__(self, name, acc_type="saving", balance=0):
        # constructor
        if not name:
            raise ValueError("Name is required")

        self.name = name
        self.type = acc_type
        self.balance = balance

        if self.type == "saving":  # saving type
            BankAccount.saving_run += 1
            # type_code = 1
            self.acc_num = f"{BankAccount.branch_number}-1-{BankAccount.saving_run}"

        elif self.type == "loan":  # loaning type
            BankAccount.loaning_run += 1
            # type_code = 2
            self.acc_num = f"{BankAccount.branch_number}-2-{BankAccount.loaning_run}"

        else:
            raise ValueError("Invalid account type")

    def get_balance(self):
        return self.balance

    def deposit(self, amount=0):  # deposit money
        self.balance += amount

    def withdraw(self, amount=0):  # withdraw money
        self.balance -= amount

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.acc_num}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance}")
        print("----- End Record -----")