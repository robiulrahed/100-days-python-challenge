"""
Problem 4: Seconds to Minutes and Seconds
Task: Given total_seconds, use // and % to convert it into
minutes and seconds, and display it nicely.
"""

total_seconds = 125

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{minutes} minutes {seconds} seconds")

# Explanation:
# - total_seconds // 60 tells us how many WHOLE minutes fit into
#   the total (125 // 60 = 2, since 60 goes into 125 twice fully).
# - total_seconds % 60 tells us what's LEFT OVER after removing
#   those whole minutes (125 % 60 = 5, the remaining seconds).
# - Together, // and % split one number into two meaningful parts -
#   this same pattern works for hours/minutes, dollars/cents, etc.
