def gcdRecur(a, b):
    """
    Input:
    a, b: positive integers

    return: a positive integer, the greatest common divisor between a & b
    """
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

"""
Used for running, do not include when submitting to the grader
"""
a = int(input("a: "))
b = int(input("b: "))
print(gcdRecur(a, b))
"""
End Runner Code
"""
