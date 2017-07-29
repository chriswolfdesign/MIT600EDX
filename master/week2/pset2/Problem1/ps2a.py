"""
Used for running, do not include when submitting to grader
"""
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
monthlyPaymentRate = float(input("Monthly Payment Rate: "))
"""
End Runner Code
"""

MONTHS = 12

monthlyInterestRate = annualInterestRate / MONTHS

for i in range(MONTHS):
    minimumPayment = monthlyPaymentRate * balance
    balance -= minimumPayment
    interest = balance * monthlyInterestRate
    balance += interest

print("Remaining balance: {}".format(round(balance, 2)))
