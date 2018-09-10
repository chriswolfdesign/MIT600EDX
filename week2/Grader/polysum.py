import math

def polysum(n, s):
    """
    n: int, number of sides
    s: int/float, the length of each side

    return: float, area + perimeter**2
    """
    numerator = 0.25 * n * (s**2)
    denominator = math.tan(math.pi / n)
    area = numerator / denominator
    perimeter = s * n
    return round(area + (perimeter**2), 4)


"""
Used for running, do not include when submitting to grader
"""
s = float(input("s: "))
n = int(input("n: "))
print(polysum(n, s))
"""
End Runner Code
"""
