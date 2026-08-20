"""
Problem 5: Balance Tracker with Assignment Operators
Task: Start with balance = 1000, add 500 using +=, subtract 300
using -=, and print balance after each step.
"""

balance = 1000
print("Starting balance:", balance)

balance += 500
print("After deposit:", balance)

balance -= 300
print("After withdrawal:", balance)

# Explanation:
# - balance += 500 is shorthand for balance = balance + 500 - it
#   takes the CURRENT value, adds 500, and saves the result back
#   into the same variable.
# - balance -= 300 works the same way with subtraction.
# - These shortcut operators are especially useful in loops (covered
#   starting Day 11/12), where a value gets updated many times.
