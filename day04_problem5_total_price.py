"""
Problem 5: Total Price Calculator
Task: Take a product's price (float) and quantity (int) as input,
calculate and print the total price.
"""

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity
print("Total Price:", total_price)

# Explanation:
# - price and quantity are converted to different numeric types
#   because price naturally has decimals (like 49.99) while quantity
#   is a whole count of items (like 3).
# - Multiplying a float by an int works fine in Python - the result
#   is automatically a float, since one operand is a float.
