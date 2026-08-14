"""
Problem 3: Two Numbers - Sum, Difference, Product
Task: Take two numbers as input (converted to float), and print their
sum, difference, and product.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

# Explanation:
# - Both inputs are converted to float, so decimal values (like 4.5)
#   work correctly, not just whole numbers.
# - Each input() call is separate - the program pauses twice, once
#   for each number, before moving on to the calculations.
