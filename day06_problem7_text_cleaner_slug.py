"""
Problem 7: Text Cleaner / Slug Generator
Task: Take a sentence as input, strip extra spaces, lowercase it,
and replace spaces with underscores to build a "slug".
Example: "Hello World" -> "hello_world"
"""

sentence = input("Enter a sentence: ")

cleaned = sentence.strip()
lowercased = cleaned.lower()
slug = lowercased.replace(" ", "_")

print("Slug:", slug)

# Explanation:
# - This chains three separate cleaning steps, each building on the
#   result of the one before it:
#   1. .strip() removes leading/trailing spaces first, so they
#      don't accidentally turn into underscores later.
#   2. .lower() makes the text consistent regardless of how the
#      user typed it (e.g. "Hello WORLD" and "hello world" become
#      the same slug).
#   3. .replace(" ", "_") swaps every remaining space with an
#      underscore, which is a common pattern for generating
#      URL-friendly or filename-friendly text.
# - This same three-step chain could be written in one line as:
#   sentence.strip().lower().replace(" ", "_")
