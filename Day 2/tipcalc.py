print("Welcome to the tip calculator!!!")
total_bill = float(input("What was the total bill?"))
per_tip = float(input("What percentage tip you would like to give?"))
split = float(input("In how many people to split the bill?"))
pay = (per_tip / 100 * total_bill + total_bill)/split
print("Each person should pay : ", round(pay,2))