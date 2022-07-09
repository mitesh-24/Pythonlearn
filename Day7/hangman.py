import random
words = ["mouse","elephant","pig"]

chosen_word = random.choice(words)

#for testing
print(f"the chosen word is {chosen_word}")

display = []

for _ in range(len(chosen_word)):
    display += ("_")
print(display)

guess = input("Enter your guess : ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    
print(display)
