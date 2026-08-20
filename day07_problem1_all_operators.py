"""
Problem 1: All Arithmetic Operators
Task: Take two numbers as input, then print their sum, difference,
product, division, floor division, and modulus.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)

# Explanation:
# - / always gives a float result, even if the numbers divide evenly.
# - // gives only the whole-number part of the division, discarding
#   anything after the decimal point.
# - % gives the remainder left over after floor division - together,
#   // and % fully describe how one number divides into another.
