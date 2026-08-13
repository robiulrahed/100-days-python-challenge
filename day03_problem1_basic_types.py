"""
Problem 1: Basic Data Type Creation
Task: Create four variables - student_name (string), student_age (int),
gpa (float), is_enrolled (bool). Print each one along with its type.
"""

student_name = "Nusrat"
student_age = 20
gpa = 3.85
is_enrolled = True

print(student_name, type(student_name))
print(student_age, type(student_age))
print(gpa, type(gpa))
print(is_enrolled, type(is_enrolled))

# Explanation:
# - student_name is text, so Python stores it as str.
# - student_age is a whole number, so it's an int.
# - gpa has a decimal point, so it's a float.
# - is_enrolled holds True/False, so it's a bool.
# - type() confirms exactly what Python decided for each variable,
#   without us ever declaring the type ourselves.
