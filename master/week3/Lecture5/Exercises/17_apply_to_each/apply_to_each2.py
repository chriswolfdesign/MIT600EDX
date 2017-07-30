"""
Used for running, do not include when submitting to grader
"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
"""
End Runner Code
"""

def addOne(x):
    """
    x: int or float

    return: x + 1
    """
    return x + 1

applyToEach(testList, addOne)

"""
Used for running, do not include when submitting to grader
"""
print(testList)
"""
End Runner Code
"""
