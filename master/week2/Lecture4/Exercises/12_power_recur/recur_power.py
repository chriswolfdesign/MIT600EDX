def recurPower(base, exp):
    """
    Input:
    base: int or float
    exp: int >= 0

    return: base^exp
    """
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

"""
Used for running, do not include when submitting to the grader
"""
base = 2
exp = 4
print(recurPower(base, exp))
"""
End Runner Code
"""
