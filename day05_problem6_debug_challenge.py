"""
Problem 6: Debug Challenge
Task: Find and fix the bug in the given code.
"""

# --- Buggy code (commented out so the file can still run) ---
# temperature = 32
# print("Todays temp is {temperature}C")
# This prints the literal text "Todays temp is {temperature}C"
# instead of showing the actual value 32.

# --- Fixed code ---
temperature = 32
print(f"Todays temp is {temperature}C")

# Explanation:
# - The original string was missing the f prefix before the opening
#   quote, so Python treated { and } as plain text characters
#   instead of a placeholder for a variable.
# - Without f, {temperature} is NOT evaluated - it's printed exactly
#   as written.
# - The fix: add f right before the opening quote so Python knows
#   to look inside { } for variables to substitute.
