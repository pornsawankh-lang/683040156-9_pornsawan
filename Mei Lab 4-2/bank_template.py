# Pornsawan Khararam
# 683040156-9

class BankAccount:
    # Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0

    __type_saving = 1
    __type_loan = 2

    def __init__(self, account_type, initial_balance=0, customer_name="Unknown"):
        self.customer_name = customer_name
        self.account_type = account_type
        self.balance = initial_balance
        if account_type.lower() == 'saving':
            BankAccount.last_saving_number += 1
            self.account_number = f"SAV-{BankAccount.last_saving_number}"
        elif account_type.lower() == 'loan':
            BankAccount.last_loan_number += 1
            self.account_number = f"LOAN-{BankAccount.last_loan_number}"
        else:
            raise ValueError("Invalid account type. Must be 'saving' or 'loan'.")

    def print_customer(self):
        print(f"Customer: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print(f"Branch: {BankAccount.branch_name} ({BankAccount.branch_number})")
    
    def deposit(self, amount=0):
        if self.account_type.lower() != 'saving':
            print("Deposit is only allowed for saving accounts.")
            return self.balance
        if amount < 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount=0):
        if self.account_type.lower() != 'saving':
            print("Withdrawal is only allowed for saving accounts.")
            return self.balance
        if amount < 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        if self.balance < amount:
            print("Insufficient balance.")
            return self.balance
        self.balance -= amount
        return self.balance
    
    def pay_loan(self, amount=0):
        if self.account_type.lower() != 'loan':
            print("Pay loan is only allowed for loan accounts.")
            return self.balance
        if amount < 0:
            print("Payment amount must be positive.")
            return self.balance
        self.balance += amount
        return self.balance
    
    def get_loan(self, amount=0):
        if self.account_type.lower() != 'loan':
            print("Get loan is only allowed for loan accounts.")
            return self.balance
        if amount < 0:
            print("Loan amount must be positive.")
            return self.balance
        if self.balance < -50000:
            print("Cannot get more loan: Balance is below -50000.")
            return self.balance
        self.balance -= amount
        return self.balance

    @classmethod
    def change_branch_name(cls, new_name):
        cls.branch_name = new_name

    @staticmethod
    def calc_interest(bal, int_rate, payment):
        print("----- Loan Plan -----")
        year = 1
        while bal > 0:
            interest = bal * (int_rate / 100)
            loan_after_interest = bal + interest
            actual_payment = min(payment, loan_after_interest)
            bal = loan_after_interest - actual_payment
            print(f"Year {year}: loan = {loan_after_interest:.2f}  payment {actual_payment:.2f}  bal = {bal:.2f}")
            year += 1
            if year > 100:  # Prevent infinite loop lmaoooo
                break
        print("----- End Plan -----")