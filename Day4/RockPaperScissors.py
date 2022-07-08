import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

set = [rock,paper,scissors]

print("It is 1 for rock, 2 for paper, and 3 for scissors")
user_choice = int(input("what is your choice?\n"))
if user_choice > 3 or user_choice < 1:
    print("Invalid Input")
    exit("Byee")
print(set [user_choice-1])

computer_choice = random.randint(1,3)
print("Computer chose")
print (computer_choice)
print(set [computer_choice-1])


if computer_choice == 1 and user_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 3:
    print("You win!")
elif user_choice == 3 and computer_choice == 2:
    print("Youu win!")
elif user_choice == computer_choice:
    print("Its a draw")
else:
    print("You loose!")
    

    
#OUTPUT


# It is 1 for rock, 2 for paper, and 3 for scissors
# what is your choice?
# 2

#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)

# Computer chose
# 3

#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# You loose!


# Test case 2

# It is 1 for rock, 2 for paper, and 3 for scissors
# what is your choice?
# 3

#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# Computer chose
# 2

#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)

# Youu win!


