"""
Problem 2: Even or Odd Checker
Task: Take a number as input, use % to check if it's even or odd,
and print the result.
"""

num = int(input("Enter a number: "))

remainder = num % 2

if remainder == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Explanation:
# - Any number divided by 2 leaves a remainder of either 0 or 1 -
#   there's no other possibility.
# - A remainder of 0 means the number divides evenly by 2, so it's
#   even. A remainder of 1 means one is "left over", so it's odd.
# - This % 2 == 0 pattern is the standard way to check evenness in
#   almost every programming language, not just Python.
