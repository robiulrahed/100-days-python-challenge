"""
Problem 6: Debug Challenge - Operator Precedence
Task: Predict the output of the expression below, then run it to check.
"""

result = 5 + 3 * 2 ** 2
print(result)

# Explanation:
# - Python follows standard math order of operations (like BODMAS/
#   PEMDAS): Parentheses, then Exponents, then Multiplication/
#   Division, then Addition/Subtraction - evaluated left to right
#   within each level.
# - Step by step:
#   1. 2 ** 2 is calculated FIRST (exponents before anything else) = 4
#   2. 3 * 4 is calculated next (multiplication before addition) = 12
#   3. 5 + 12 is calculated last = 17
# - So the answer is 17, NOT 32 (which you'd get by evaluating
#   strictly left to right ignoring precedence: 5+3=8, 8*2=16, 16**2=256 -
#   also wrong, showing how easy it is to misjudge without knowing
#   the precedence rules).
