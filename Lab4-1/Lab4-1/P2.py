"""
Pornsawan Khareram
683040156-9
"""

from bank_acc import BankAccount


john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim",  'loan', -10000)
sarah = BankAccount("Sarah", "saving")

john.deposit(3000)
print(f"john balance: {john.get_balance():,}\n")

print(f"Tim loan: {tim.get_balance():,}\n")
tim.withdraw(5000)
print("After payment: {tim.get_balance():,}\n")


sarah.deposit(50000000)
sarah_loan = BankAccount("sarah", "loan", "-100000000")

john.print_customer()
print()
tim.print_customer()
print()
sarah.print_customer()
print()
sarah.print_customer()
print()