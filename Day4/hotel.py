import random
name_string = input("Input the names of the people between whom u want to split the bill :")
names = name_string.split(", ")
count = len(names)
print(names[random.randint(0, (count-1))], "will pay the bill")

# We van also use random.choice() method to get a random name from a list

# print(random.choice(names))