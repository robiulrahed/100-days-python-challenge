"""
Problem 4: Name and City Sentence
Task: Take name and city as input, and print "[name] lives in [city]."
"""

name = input("Enter your name: ")
city = input("Enter your city: ")

print(name + " lives in " + city + ".")

# Explanation:
# - Both name and city come from input(), so both are already strings,
#   which is why they can be joined directly with + and no type
#   conversion is required here (unlike when working with numbers).
# - Notice the extra " " and "." are added manually to build a
#   properly spaced, punctuated sentence.
