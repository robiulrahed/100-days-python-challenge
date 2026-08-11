"""
Problem 3: Special Characters
Task: Reproduce a formatted output using \\n (new line) and \\t (tab space).
"""

# Method 1: Using three separate print() statements with \t
print("Name:\tJohn")
print("Age:\t25")
print("City:\tDhaka")

print("\n--- Same output using a single print() with \\n ---\n")

# Method 2: Using a single print() with \n to create new lines
print("Name:\tJohn\nAge:\t25\nCity:\tDhaka")

# Explanation:
# - \t inserts a tab space, which is useful for aligning text in columns.
# - \n inserts a new line, letting us create multi-line output from
#   a single print() statement instead of using multiple print() calls.
# - Both methods above produce the same visual result.
