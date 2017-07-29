"""
Used for running, do not include when submitting to grader
"""
balance = int(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
"""
End Runner Code
"""

EPSILON = 0.01
MONTHS = 12
monthlyInterestRate = annualInterestRate / MONTHS
lowerBound = balance / MONTHS
upperBound = (balance * (1 + monthlyInterestRate)**MONTHS) / MONTHS
paymentGuess = (lowerBound + upperBound) / 2
balanceTmp = balance

while abs(balanceTmp) >= EPSILON:

    # Reset our balance to try again
    balanceTmp = balance

    for i in range(MONTHS):
        balanceTmp -= paymentGuess
        interest = balanceTmp * monthlyInterestRate
        balanceTmp += interest

    # if we were not paying enough, pay more
    if balanceTmp > 0:
        lowerBound = paymentGuess

    # if we were paying too much, pay less
    else:
        upperBound = paymentGuess

    paymentGuess = (lowerBound + upperBound) / 2

print("Lowest Payment: {}".format(round(paymentGuess, 2)))
