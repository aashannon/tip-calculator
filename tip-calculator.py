# Day 2
# Creating a tip calculator
# Practicing input, variables, arithmetic operations, and f-strings

print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip would you like to give? e.g. 10, 12, 15\n"))
people_count = int(input("How many people are splitting the bill?\n"))

total_bill = bill + (bill * tip/100)
per_person = total_bill / people_count

print(f"Each person should pay: ${round(per_person, 2)}")
