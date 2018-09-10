"""
Used for running, do not include when submitting to grader.
"""

x = int(input("x: "))
a = int(input("a: "))

"""
End Runner Code
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

"""
Used for running, do not include when submitting to grader.
"""

print(integerDivision(x, a))

"""
End Runner Code
"""
