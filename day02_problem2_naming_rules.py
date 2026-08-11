"""
Problem 2: Naming Rule Spotting
Task: Identify which variable names are valid or invalid, and explain why.
"""

# 1. 2024_sales      -> INVALID (starts with a digit)
# 2. user-id         -> INVALID (hyphens are not allowed, use underscore)
# 3. _count          -> VALID (can start with an underscore)
# 4. class           -> INVALID (it's a reserved Python keyword)
# 5. totalAmount      -> VALID (camelCase is allowed, though snake_case
#                         is the preferred convention in Python)
# 6. my var          -> INVALID (spaces are not allowed in variable names)

# Corrected versions of the invalid ones:
sales_2024 = 1500       # instead of 2024_sales
user_id = "U1023"       # instead of user-id
class_name = "Physics"  # instead of class
my_var = 42              # instead of "my var"

print(sales_2024)
print(user_id)
print(class_name)
print(my_var)

# Explanation:
# - Variable names cannot start with a digit, contain spaces, contain
#   hyphens, or be one of Python's reserved keywords (if, for, class, etc).
# - They CAN start with a letter or underscore, and can mix letters,
#   digits, and underscores after the first character.
