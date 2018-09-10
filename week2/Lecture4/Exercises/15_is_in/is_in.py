def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    return: True if char in aStr; False otherwise
    """
    if len(aStr) < 1:
        return False
    mid = len(aStr) // 2
    if aStr[mid] == char:
        return True
    elif len(aStr) == 1:
        return False
    elif aStr[mid] < char:
        return isIn(char, aStr[mid:])
    elif aStr[mid] > char:
        return isIn(char, aStr[:mid])

"""
Used for running, do not include when submitting to grader.
"""
char = input("char: ")
aStr = input("aStr: ")
print(isIn(char, aStr))
