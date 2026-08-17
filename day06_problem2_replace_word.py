"""
Problem 2: Replace a Word
Task: Create sentence = "I love JavaScript", replace "JavaScript"
with "Python" using .replace(), and print the result.
"""

sentence = "I love JavaScript"
updated_sentence = sentence.replace("JavaScript", "Python")

print(updated_sentence)

# Explanation:
# - .replace(old, new) scans the string for every occurrence of
#   "old" and swaps it with "new", returning a new string.
# - The original sentence variable is untouched; we store the
#   result in a new variable, updated_sentence, to use it.
