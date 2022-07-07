print("Welcome to Giant Rollercoaster!!!")
height = int(input("What is your Height?"))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 10
        print("Youth tickets are $10")
    elif age > 45 & age < 55 :
        bill = 0
    else:
        bill = 15
        print("Adult tickets are $15")
    
    photo = input ("Do you want to take a photo? Y/N ")
    if photo == "Y":
        bill += 3

        print(f"Your total bill is {bill}")

else:
    print("You can't ride the Rollercoaster")