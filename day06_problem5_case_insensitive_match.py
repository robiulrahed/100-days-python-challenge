"""
Problem 5: Case-Insensitive Match
Task: Take input that might be "yes", "YES", or "Yes" in any case,
convert to lowercase, check if it matches "yes", and print the result.
"""

answer = input("Do you want to continue? (yes/no): ")

if answer.lower() == "yes":
    print("Matched")
else:
    print("Not matched")

# Explanation:
# - Users might type Yes, YES, yes, or even YeS - all meaning the
#   same thing, but Python treats them as different strings by
#   default since string comparison is case-sensitive.
# - .lower() normalizes the input to all-lowercase BEFORE comparing,
#   so "YES", "Yes", and "yes" all become "yes" and match correctly.
# - Note: if/else itself will be covered in detail on Day 9 - here
#   it's used just to show a practical use case for .lower().
