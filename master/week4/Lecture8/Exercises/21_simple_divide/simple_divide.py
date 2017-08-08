"""
Used for running, do not include when submitting to grader
"""
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]
"""
End Runner Code
"""

def simple_divide(item, denom):
    try:
        return item/denom
    except ZeroDivisionError:
        return 0

"""
Used for running, do not include when submitting to grader
"""
answer = fancy_divide([0, 2, 4], 0)
print(answer)
"""
End Runner Code
"""
