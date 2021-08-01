total_bill = float(input("What was the total bill? $"))
people = float(input("How many people splitting the bill\n"))
percentage = float(input("What percentage of tip you would give? 10 15 or 20?\n"))

cal = (total_bill + (percentage / 100 * total_bill)) / people 

print(F"Each person should pay {cal}")
