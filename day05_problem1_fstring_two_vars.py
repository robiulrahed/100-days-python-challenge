"""
Problem 1: f-string with Two Variables
Task: Create name and profession variables, then use an f-string to
print "I am [name], working as a [profession]."
"""

name = "Rima"
profession = "Software Developer"

print(f"I am {name}, working as a {profession}.")

# Explanation:
# - The f before the opening quote tells Python this is an f-string,
#   allowing variables to be embedded directly using { } brackets.
# - Python replaces {name} and {profession} with their current values
#   at the moment print() runs - no manual + concatenation needed.
