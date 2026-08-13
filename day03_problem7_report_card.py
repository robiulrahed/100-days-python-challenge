"""
Problem 7: Real-world Application - Student Report Card
Task: Build a program with student_name, roll_number, percentage,
and is_passed (True if percentage > 40).
"""

student_name = "Farhan Ahmed"
roll_number = 24
percentage = 78.5
is_passed = percentage > 40

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage)
print("Passed:", is_passed)

# Explanation:
# - student_name -> string, roll_number -> int, percentage -> float,
#   matching the data they represent.
# - is_passed is not typed in manually as True/False; it's calculated
#   using a comparison: percentage > 40. This comparison itself
#   produces a boolean value (True or False), which gets stored
#   directly in is_passed.
# - This shows how bool values often come from conditions/comparisons
#   rather than being written directly - a preview of what we'll use
#   heavily starting Day 9 (if/else statements).
