import random
import os
from word_list import get_word_list  # type: ignore

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

word_list = get_word_list()
print(r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
""")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_choice=random.choice(word_list)

lives = 6
end_of_game = False
print("You have to guess:")
display = []
for check in random_choice:
  display.append("_")
print(f"{' '.join(display)}\n")

print("If you guess a letter that's not in the word you lose a life")

while( not end_of_game):
    guess=input("Guess a letter: ").lower()
    clear_screen()
    if guess in display:
       print(f"You've already guessed {guess}. Try another letter.")

    for position in range(len(random_choice)):
       if random_choice[position] == guess:
          display[position] = guess

    if guess not in random_choice:
        print(f"the letter {guess} is not in the word. so you lose a life")
        print(stages[lives])
        lives -= 1
        if lives == -1:
            end_of_game = True
            print("You lose.")
            print(f"The corrcet word was {random_choice}")
            quit()

    print(f"{' '.join(display)}")

    if "_" not in display:
       end_of_game = True
       print("You win.")
       quit()