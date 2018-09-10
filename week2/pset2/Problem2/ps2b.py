"""
Used for running, do not include when submitting to grader
"""
balance = int(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
"""
End Runner Code
"""

MONTHS = 12
balanceTmp = balance
monthlyInterestRate = annualInterestRate / MONTHS
paymentGuess = 0

while balanceTmp > 0:
    balanceTmp = balance
    paymentGuess += 10

    for i in range(MONTHS):
        balanceTmp -= paymentGuess
        interest = monthlyInterestRate * balanceTmp
        balanceTmp += interest

print("Lowest Payment: {}".format(paymentGuess))
