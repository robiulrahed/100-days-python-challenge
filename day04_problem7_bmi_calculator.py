"""
Problem 7: Simple BMI Calculator
Task: Take weight (kg, float) and height (meters, float) as input,
calculate and display BMI.
Formula: BMI = weight / (height * height)
"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)
print("Your BMI is:", bmi)

# Explanation:
# - Both weight and height must be floats since they're rarely whole
#   numbers (e.g. 68.5 kg, 1.72 m).
# - The formula uses (height * height) instead of an exponent operator
#   for clarity - Python does support height ** 2 as well, which
#   means the same thing and will be covered when we look at
#   arithmetic operators in more depth on Day 7.
# - Division (/) between two floats returns a float result, which is
#   exactly what BMI should be (a decimal number).
