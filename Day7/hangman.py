import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
words = ["mouse","elephant","pig"]
chosen_word = random.choice(words)
word_length = (len(chosen_word))

lives = 6
#for testing
print(f"pssst the chosen word is {chosen_word}")

display = []

for _ in range(word_length):
    display += ("_")

while not end_of_game:
    guess = input("Enter your guess : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!!")
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You won!")
        
    print(stages[lives])
