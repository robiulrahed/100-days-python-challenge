"""
Problem 4: Negative Indexing
Task: Using the same word variable, print the last 3 characters
using negative indexing ([-1], [-2], [-3]).
"""

word = "Programming"

print(word[-1])   # last character
print(word[-2])   # second-to-last character
print(word[-3])   # third-to-last character

# Explanation:
# - Negative indexing counts from the END of the string, starting
#   at -1 for the last character.
# - word[-1] is 'g', word[-2] is 'n', word[-3] is 'i' - moving one
#   position further back with each step.
# - This is very useful when you don't know (or don't want to
#   calculate) the exact length of a string.
