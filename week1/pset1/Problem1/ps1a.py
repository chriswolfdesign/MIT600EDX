"""
Used for running, do not include when submitting to grader.
"""
s = "azcbobobegghakl"
"""
End Runner Code
"""
num = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
        num += 1

print("Number of vowels: {}".format(num))
