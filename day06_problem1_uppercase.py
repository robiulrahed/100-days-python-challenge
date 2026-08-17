"""
Problem 1: Uppercase Conversion
Task: Store your name in lowercase, then print it in uppercase
using .upper().
"""

name = "rahed"
print(name.upper())

# Explanation:
# - .upper() returns a NEW string with every letter converted to
#   uppercase - it does not change the original name variable.
# - Since we only print the result here (not reassign it), name
#   itself would still be "rahed" if printed again separately.
