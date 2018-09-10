"""
Used for running, do not include when submitting to the grader
"""
a = 5
b = 4
c = 3
x = 2
"""
End Runner Code
"""

def evalQuadratic(a, b, c, x):
    """
    a, b, c: numberical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic
    return: the solution for the quadratic equation at x
    """
    return (a * x**2) + (b * x) + c

"""
Used for running, do not include when submitting to the grader
"""
print(evalQuadratic(a, b, c, x))
"""
End Runner Code
"""
