"""
Problem 6: Debug Challenge
Task: Find and fix the bug - the code should ADD two numbers,
but instead joins them as text.
"""

# --- Buggy code (commented out so the file can still run) ---
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# print(num1 + num2)
# If the user enters 5 and 3, this prints "53" instead of 8!

# --- Fixed code ---
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

# Explanation:
# - Without int(), both num1 and num2 are strings, so the + operator
#   performs string CONCATENATION (joining text) instead of addition.
#   Entering 5 and 3 gives "5" + "3" = "53", not 5 + 3 = 8.
# - Wrapping each input() with int() converts the text into real
#   numbers first, so + now performs mathematical addition.
