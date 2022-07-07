size = input("Enter the size of the pizza you want to have :")
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

pep = input("Want pepperoni?")

if pep == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

cheese = input("Want extra cheese?")

if cheese == 'Y':
    bill += 1


print(f"Your bill is {bill}")