"""
Problem 2: Age After 10 Years
Task: Take age as input (converted to int), calculate age after
10 years, and print it.
"""

age = int(input("Enter your age: "))
age_after_10_years = age + 10

print("In 10 years, you will be", age_after_10_years, "years old.")

# Explanation:
# - input() alone would give age as a string like "20", and
#   "20" + 10 would raise a TypeError.
# - Wrapping input() with int() converts the typed text into a real
#   number BEFORE it's stored in age, so age + 10 works correctly
#   as a mathematical addition.
