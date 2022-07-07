weight = float(input("Enter your weight in Kg. : "))
height = float(input("Enter your height in meters : "))

bmi = round(weight / (height**2))

print(bmi)

if bmi < 18.5 :
    print("You are underweight.")
elif bmi > 18.5 & bmi < 25 :
    print("Normal weight.")
elif bmi > 25 & bmi < 30 :
    print("Overweight.")
elif bmi > 30 & bmi < 35 :
    print("Obese.")
elif bmi > 35 :
    print("Clinically Obese.")