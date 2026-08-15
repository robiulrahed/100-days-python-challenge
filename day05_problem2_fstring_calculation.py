"""
Problem 2: f-string with Calculation
Task: Store two numbers in variables, multiply them directly inside
an f-string, and display the result.
"""

x = 8
y = 6

print(f"Result: {x * y}")

# Explanation:
# - The { } in an f-string doesn't just hold a variable name - it can
#   hold any valid Python expression, including math operations.
# - Python evaluates x * y first (8 * 6 = 48), then inserts that
#   result into the string, all in a single line.
