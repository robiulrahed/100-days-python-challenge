"""
Problem 7: Bill Splitter
Task: Take a total bill amount and number of people as input,
calculate the equal share per person using //, and calculate
any leftover amount using %.
"""

total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))

# Convert to int (paisa/cents-free) for clean floor division and
# modulus on whole currency units:
total_bill_int = int(total_bill)

share_per_person = total_bill_int // num_people
leftover = total_bill_int % num_people

print(f"Each person pays: {share_per_person}")
print(f"Leftover amount (not evenly divisible): {leftover}")

# Explanation:
# - // gives each person's EQUAL whole-number share of the bill,
#   ignoring any remainder for now.
# - % gives whatever amount is LEFT OVER after that equal split -
#   this is the extra amount that doesn't divide evenly and would
#   need to be handled separately (e.g. one person pays a bit more,
#   or it gets added as a tip).
# - Example: a bill of 100 split 3 ways gives 33 each (// result)
#   with 1 leftover (% result), since 33 * 3 = 99, not 100.
