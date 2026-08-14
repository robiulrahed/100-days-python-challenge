"""
Problem 1: Basic Input & Greeting
Task: Take the user's name as input and print "Hello, [name]! Welcome."
"""

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome.")

# Explanation:
# - input() pauses the program, shows the prompt text, and waits for
#   the user to type something and press Enter.
# - Whatever the user types is returned as a string and stored in name.
# - We build the final message by joining ("concatenating") strings
#   with the + operator - this only works because name is already
#   a string, so no type conversion is needed here.
