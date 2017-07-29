"""
Used for running, do not include when submitting to grader
"""
aTup = ('I', 'am', 'a', 'test', 'tuple')
"""
End Runner Code
"""

def oddTuples(aTup):
    """
    aTup: a tuple

    return: a tuple, every other element of aTup
    """
    answer = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            answer = answer + (aTup[i],)

    return answer

"""
Used for running, do not include when submitting to grader
"""
print(oddTuples(aTup))
"""
End Runner Code
"""
