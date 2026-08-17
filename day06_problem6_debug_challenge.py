"""
Problem 6: Debug Challenge
Task: Find and fix the bug - the code should print "PYTHON" but
prints "python" instead.
"""

# --- Buggy code (commented out so the file can still run) ---
# word = "python"
# word.upper()
# print(word)
# This prints "python" (unchanged) instead of "PYTHON"

# --- Fixed code ---
word = "python"
word = word.upper()
print(word)

# Explanation:
# - word.upper() DOES create an uppercase version of the string,
#   but that result was never saved anywhere in the buggy code -
#   it was calculated and then immediately thrown away.
# - String methods never modify the original string in place
#   (strings are immutable in Python), so you must reassign the
#   result back to a variable to actually keep it: word = word.upper().
