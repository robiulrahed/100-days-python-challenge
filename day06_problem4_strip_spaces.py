"""
Problem 4: Strip Extra Spaces
Task: Take input that may have extra leading/trailing spaces,
clean it with .strip(), and show before vs after.
"""

user_input = input("Enter your name (extra spaces are OK): ")

print(f"Before strip: '{user_input}'")
print(f"After strip: '{user_input.strip()}'")

# Explanation:
# - The quotes ' ' around the printed value make any extra spaces
#   visible, which is why they're added here - normally you
#   wouldn't need them.
# - .strip() only removes spaces from the very START and END of
#   the string - it does NOT remove spaces in the middle
#   (e.g. "Md   Rahed" keeps its middle spaces).
