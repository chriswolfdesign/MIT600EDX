def gcdIter(a, b):
    """
    Input:
    a, b: positive integers

    return: a positive integer, greatest common divisor of a & b
    """
    if a < b:
        num = a
    else:
        num = b
    while num > 0:
        if a % num == 0 and b % num == 0:
            return num
        else:
            num -= 1

"""
Used for running, do not include when submitting to the grader.
"""
a = int(input("a: "))
b = int(input("b: "))
print(gcdIter(a, b))
"""
End Runner Code
"""
