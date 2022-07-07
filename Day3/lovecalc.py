print("Welcome to the Love Calculator!")
name1 = input("Enter your name : ")
name2 = input("Enter your Crush's name : ")

combined_name = name1 + name2
combined_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

love_score = (true + love)*5
print(f"Your Love Score is {love_score}")
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print("You go together like Coke and Mentos!!!")
elif love_score > 40 & love_score < 50:
    print("You both are alright together!!!")