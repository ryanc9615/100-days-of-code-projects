print("Welcome to tip calculator!")
total_bill = int(input("What was the total bill? $ "))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15?"))
num_people = int(input("How many people to split the bill?"))
calculation = (total_bill + (tip_amount * (total_bill)/100))/num_people
print(f"Each person would pay: ${calculation}")