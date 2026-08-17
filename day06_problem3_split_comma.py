"""
Problem 3: Split by Comma
Task: Create data = "Dhaka,Chittagong,Sylhet", split it by comma
into a list, and print it.
"""

data = "Dhaka,Chittagong,Sylhet"
cities = data.split(",")

print(cities)

# Explanation:
# - .split(",") breaks the string apart everywhere a comma appears,
#   and returns the pieces as a list of strings.
# - The comma itself is removed from the result - it's used only
#   as the "cut point", not kept in the output.
# - Lists will be covered in detail starting Day 21, but this is a
#   preview of how a string becomes a list of separate items.
