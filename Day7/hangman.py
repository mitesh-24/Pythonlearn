import random
words = ["mouse","elephant","pig"]

chosen_word = random.choice(words)

guess = input("Enter your guess : ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")