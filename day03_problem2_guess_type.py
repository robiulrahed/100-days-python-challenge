"""
Problem 2: Guess the Data Type
Task: Guess the data type of each variable below, then verify with type().
"""

a = 42
b = 'True'
c = 3.0
d = False

print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))
print(d, "->", type(d))

# Explanation:
# - a = 42 is a whole number -> int
# - b = 'True' LOOKS like a boolean, but it's wrapped in quotes,
#   so Python treats it as a string, not a real True/False value.
#   This is a common trap: quotes always mean string, no matter
#   what the text inside looks like.
# - c = 3.0 has a decimal point, so it's a float, even though the
#   value is a whole number mathematically.
# - d = False (no quotes) is a real boolean.
