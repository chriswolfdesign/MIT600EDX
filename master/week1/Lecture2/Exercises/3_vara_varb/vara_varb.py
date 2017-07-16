"""
Used for running, do not include when submitting to grader
"""

vara = 6
varb = 5

"""
End Runner Code
"""

string_var = "I'm a string!"

if (type(varA) == type(string_var)) or (type(varB) == type(string_var)):
    print("string involved")
elif varA == varB:
    print("equal")
elif varA > varB:
    print("bigger")
else:
    print("smaller")
