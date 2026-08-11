"""
Problem 6: Debug Challenge
Task: Find and fix the variable naming rule violation.
"""

# --- Buggy code (commented out so the file can still run) ---
# 1st_place = "Karim"
# print(1st_place)

# --- Fixed code ---
first_place = "Karim"
print(first_place)

# Explanation:
# - The original code `1st_place = "Karim"` breaks the rule that
#   variable names cannot start with a digit.
# - This causes a SyntaxError, because Python tries to interpret "1"
#   as the start of a number, not a variable name.
# - The fix: rename it to start with a letter, such as first_place,
#   while still keeping the meaning clear.
