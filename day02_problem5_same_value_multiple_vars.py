"""
Problem 5: Same Value, Multiple Variables
Task: Assign the same value (100) to three variables (a, b, c) in one
line, then print each one.
"""

a = b = c = 100

print(a)
print(b)
print(c)

# Explanation:
# - Chaining assignment with `a = b = c = 100` assigns 100 to all three
#   variables at once, because Python evaluates the assignment from
#   right to left: c gets 100, then b gets c's value, then a gets b's value.
# - This is different from Problem 3, where each variable got a
#   DIFFERENT value using commas. Here, all three share the SAME value.
