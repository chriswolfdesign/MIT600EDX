"""
Used for running, do not include when submitting to grader.
"""
s = "abcbcd"
"""
End Runner Code
"""

longest_substring = s[0]
current_substring = s[0]

for letter in range(1, len(s)):
    if s[letter] >= s[letter - 1]:
        current_substring += s[letter]
    else:
        current_substring = s[letter]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print("Longest substring in alphabetical order is: {}".\
    format(longest_substring))
