def iterPower(base, exp):
    """
    base: int or float
    exp: int >= 0

    return: base^exp
    """
    num = 1
    for i in range(exp):
        num *= base
    return num

"""
Used for running, do not include when submitting to grader
"""
base = 2
exp = 4
print(iterPower(base, exp))
"""
End Runner Code
"""
