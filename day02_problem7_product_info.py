"""
Problem 7: Real-world Application
Task: Build a small "product info" program with product_name,
product_price, quantity, and a calculated total_price.
"""

product_name = "Wireless Mouse"
product_price = 15.50
quantity = 3

total_price = product_price * quantity

print("Product Name:", product_name)
print("Unit Price:", product_price)
print("Quantity:", quantity)
print("Total Price:", total_price)

# Explanation:
# - total_price is not typed in directly; it's calculated from other
#   variables using the * (multiplication) operator.
# - This shows a key use of variables: once product_price and quantity
#   are stored, we can reuse them in calculations instead of
#   hardcoding numbers, and the result stays accurate if either
#   value changes later.
