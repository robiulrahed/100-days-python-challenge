"""
Problem 6: Debug Challenge
Task: Find and fix the bug in the given code.
"""

# --- Buggy code (commented out so the file can still run) ---
# is_active = true
# print(is_active)

# --- Fixed code ---
is_active = True
print(is_active)

# Explanation:
# - The original code used `true` with a lowercase "t", but Python's
#   boolean values are `True` and `False`, both starting with a
#   capital letter.
# - This causes a NameError: name 'true' is not defined, because
#   Python thinks `true` is a variable name that was never created,
#   not the boolean value.
# - The fix: always capitalize True and False in Python.
