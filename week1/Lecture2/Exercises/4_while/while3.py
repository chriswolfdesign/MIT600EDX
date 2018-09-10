"""
Used for running, do not include while submitting to grader
"""
end = int(input("Enter int: "))
"""
End Runner
"""

total = 0
count = 1
while count <= end:
    total += count
    count += 1
print(total)
