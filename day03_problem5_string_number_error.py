"""
Problem 5: String + Number Error
Task: Create a string variable holding a number, try marks + 10 directly,
observe the error, then find a way to fix it.
"""

marks = "85"

# --- This line would cause an error if uncommented ---
# print(marks + 10)
# TypeError: can only concatenate str (not "int") to str

# --- The fix: convert marks to int first ---
fixed_result = int(marks) + 10
print(fixed_result)

# Explanation:
# - marks = "85" is a string, even though it looks like a number.
# - Python does not automatically convert strings to numbers during
#   math operations, so marks + 10 fails with a TypeError, because
#   you cannot add a string and an integer directly.
# - The fix is to explicitly convert marks using int(marks) before
#   adding, which turns "85" into the real number 85.
