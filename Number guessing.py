import random

print("""
      Welcome to the Number Guessing Game!
      I'm thinking of a number between 1 and 100.
      """)

computer_guess = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def check(num,cnum):
    if num == cnum:
        return "True"
    elif num > cnum:
        return "high"
    else:
        return "low"
    
def nochances(num):
    num -= 1
    return num

end_of_loop = False

while not end_of_loop:
    if difficulty == "hard":
        chances = 5
        end_of_loop = True
    elif difficulty == "easy":
        chances = 10
        end_of_loop = True
    else:
        print("you choosed an invalid choice")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

end_of_game =False

while not end_of_game:
    print(f"You have {chances} attempts remaining to guess the number.")
    your_guess = int(input("Make a guess:"))
    if(check(your_guess, computer_guess) == "True"):
        print(f"You got it! The answer was {computer_guess}.")
        end_of_game = True
    else:
        chances = nochances(chances)
        print(f"the number you guessed is '{check(your_guess, computer_guess)}' ")
        if chances == 0:
            print("You've run out of guesses, you lose.")