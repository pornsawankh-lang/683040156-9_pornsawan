# Pornsawan Khararam
# 683040156-9

from bank_template import BankAccount

saving_acc = BankAccount("saving", 1000, "Meiii")
loan_acc = BankAccount("loan", -2000, "TeH")  

print("--- Saving Account ---")
saving_acc.print_customer()

print("\n--- Loan Account ---")
loan_acc.print_customer()

print("\n--- Operations ---")
print(f"Alice deposits 500: New balance = {saving_acc.deposit(500)}")
print(f"Alice withdraws 200: New balance = {saving_acc.withdraw(200)}")

print(f"Bob pays loan 300: New balance = {loan_acc.pay_loan(300)}")
print(f"Bob gets loan 1000: New balance = {loan_acc.get_loan(1000)}")

BankAccount.change_branch_name("New KKU Branch")
print(f"Updated branch name: {BankAccount.branch_name}")

print("\n--- Loan Interest Calculation ---")
BankAccount.calc_interest(1000, 5, 100)