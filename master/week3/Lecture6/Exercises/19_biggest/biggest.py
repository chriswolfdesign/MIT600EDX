"""
Used for running, do include when submitting to grader
"""
animals = {'a': ["aardvark"], 'b': ["baboon"], 'c': ["coati"]}
animals['d'] = ["donkey"]
animals['d'].append("dog")
animals['d'].append("dingo")
"""
End Runner Code
"""

def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    return: The key with the largest number of values associated with it
    """

    largest_index = None
    largest_count = 0
    for item in aDict:
        if len(aDict[item]) > largest_count:
            largest_index = item
            largest_count = len(aDict[item])
    return largest_index

"""
Used for running, do not include when submitting to grader
"""
print(biggest(animals))
"""
End Runner Code
"""
