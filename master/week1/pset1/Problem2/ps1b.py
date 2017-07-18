"""
Used for running, do not include when submitting to grader
"""
s = "azcbobobegghakl"
"""
End Runner Code
"""
bobs = 0

for letter in range(len(s)):
    if s[letter: letter + 3] == "bob":
        bobs += 1

print("Number of times bob occurs is: {}".format(bobs))
