"""
Problem 5: First Letter of User's Name
Task: Take the user's name as input, then use f-string + indexing
to show what the first letter is.
"""

name = input("Enter your name: ")

print(f"The first letter of your name is {name[0]}")

# Explanation:
# - name comes from input(), so it's already a string, and strings
#   can be indexed directly just like any other string.
# - name[0] grabs the first character, and the f-string embeds that
#   single character directly into the sentence.
# - This combines two Day 5 concepts (f-strings and indexing) in
#   one line, which is a very common real-world pattern.
