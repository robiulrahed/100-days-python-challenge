"""
Problem 6: Error Spotting (Debug Challenge)
Task: Find and fix the bug in the given code.
"""

# --- Buggy code (commented out so the file can still run) ---
# print("Hello, World!)

# --- Fixed code ---
print("Hello, World!")

# Explanation:
# - The original code had a missing closing quotation mark:
#     print("Hello, World!)
#   The string starts with " but never closes with a matching ".
# - This causes a SyntaxError: EOL while scanning string literal,
#   because Python doesn't know where the string is supposed to end.
# - The fix: always make sure quotes come in matching pairs,
#   either "..." or '...', both opened and closed correctly.
