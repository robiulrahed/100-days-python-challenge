"""
Problem 3: String to Int Conversion
Task: Convert the string '100' into a number using int(), add 50 to it,
and print the result.
"""

value_str = "100"
value_int = int(value_str)

result = value_int + 50
print(result)

# Explanation:
# - "100" is a string (text that looks like a number), so it cannot
#   be used directly in math operations.
# - int("100") converts it into a real integer, 100.
# - Once converted, it behaves like any other number and can be
#   added, subtracted, etc. Here 100 + 50 gives 150.
