"""
Problem 3: Basic Indexing
Task: Create word = "Programming", then print the first character,
last character, and the character at index 4.
"""

word = "Programming"

print("First character:", word[0])
print("Last character:", word[len(word) - 1])
print("Character at index 4:", word[4])

# Explanation:
# - word[0] gets the very first character - indexing always starts
#   counting from 0, not 1.
# - The last character's index is always (length - 1), since indexes
#   go from 0 up to length-1. len(word) gives 11, so index 10 is last.
# - word[4] counts P-r-o-g-r, landing on 'r' (the 5th character,
#   at index position 4).
