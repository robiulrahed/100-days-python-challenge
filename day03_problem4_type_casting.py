"""
Problem 4: Type Casting Practice
Task: Create an int variable num = 7, convert it to float and string
using float() and str(), and print the type of each result.
"""

num = 7
print(num, type(num))

num_float = float(num)
print(num_float, type(num_float))

num_str = str(num)
print(num_str, type(num_str))

# Explanation:
# - float(num) converts 7 into 7.0 - same value, but now stored
#   with decimal precision.
# - str(num) converts 7 into the text "7" - it can now be joined
#   with other text (concatenated), but can no longer be used
#   directly in math operations without converting it back.
# - The original num variable itself is never changed; each
#   conversion function returns a NEW value in the new type.
