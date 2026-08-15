"""
Problem 7: Username Generator
Task: Take the user's name and birth year as input, then use
f-string + indexing to build a username from the first 3 letters
of the name plus the birth year.
"""

name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

first_three_letters = name[0] + name[1] + name[2]
username = f"{first_three_letters}{birth_year}"

print(f"Your generated username is: {username}")

# Explanation:
# - name[0], name[1], name[2] individually grab the 1st, 2nd, and
#   3rd characters, which are then joined together with +.
# - birth_year comes from input(), so it's already a string - no
#   conversion needed here since we're not doing math with it,
#   just joining text.
# - The final f-string combines both pieces into one username,
#   showing how indexing and f-strings work together in a
#   realistic small program.
