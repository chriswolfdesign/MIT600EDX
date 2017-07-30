"""
Used for running, do not include when submitting to grader
"""
animals = {'a': ["aardvark"], 'b': ["baboon"], 'c': ["coati"]}
animals['d'] = ["donkey"]
animals['d'].append("dog")
animals['d'].append("dingo")
"""
End Runner Code
"""

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    return: int, how many values are in the dictionary.
    """
    total = 0
    for item in aDict:
        total += len(aDict[item])
    return total

"""
Used for running, do not include when submitting to grader
"""
print(how_many(animals))
"""
End Runner Code
"""
