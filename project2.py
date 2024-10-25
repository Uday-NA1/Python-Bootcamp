print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill with? "))
tip = tip_percent / 100 * bill
bill_with_tip =  tip + bill
bill_per_person = bill_with_tip / people
round(bill_per_person, 2)
print(bill_per_person)