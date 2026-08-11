"""
Problem 4: Value Update
Task: Create a balance variable with value 1000, subtract 250, and
print the value before and after the update.
"""

balance = 1000
print("Before:", balance)

balance = balance - 250
print("After:", balance)

# Explanation:
# - The line `balance = balance - 250` first calculates the right-hand
#   side (1000 - 250 = 750) using the CURRENT value of balance,
#   then assigns that new result back to balance.
# - This is why the "before" and "after" prints show different values:
#   the variable was reassigned, not just displayed differently.
