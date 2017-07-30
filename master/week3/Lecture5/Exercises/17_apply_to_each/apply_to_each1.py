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

applyToEach(testList, abs)

"""
Used for running, do not include when submitting to grader
"""
print(testList)
"""
End Runner Code
"""
