"""
Problem 3: Power Calculator
Task: Take base and exponent as input, use ** to calculate the power,
and display the result.
"""

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = base ** exponent
print(f"{base} to the power of {exponent} is {result}")

# Explanation:
# - The ** operator raises the left number to the power of the
#   right number: base ** exponent means base multiplied by itself
#   exponent times.
# - For example, 2 ** 3 means 2 * 2 * 2 = 8, not 2 * 3 = 6 - it's
#   easy to confuse ** with multiplication, but they're different.
