import random
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check(score):
    return score >= 21
    
def close_21(num1, num2):
    target = 21
    diff1 = (target - num1)
    diff2 = (target - num2)
    if (diff1 < diff2):
        return num1
    elif (diff1 > diff2):
        return num2
    else:
        return None
    
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

end_of_program = False

start_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
if start_game != "y":
    end_of_program = True
    print("Then why did come yaar!")

while not end_of_program:
    print(logo)

    your_cards = random.choices(cards, k = 2)
    your_score = calculate_score(your_cards)
    print(f"Your cards:{your_cards}  current score:{your_score}")

    computers_cards = random.choices(cards, k = 2)
    comp_score = calculate_score(computers_cards)
    print(f"Computer's first card:[{computers_cards[0]}]")

    while not check(your_score):
        addcard=input("Type 'y' to get another card, type 'n' to pass:").lower()
        if addcard == "y":
            your_cards.append(random.choice(cards))
            your_score = calculate_score(your_cards)
            print(f"Your cards:{your_cards}  current score:{your_score}")
            print(f"Computer's first card:[{computers_cards[0]}]")
        else:
            break

        while comp_score < 17:
            computers_cards.append(random.choice(cards))
            comp_score = calculate_score(computers_cards)

        print(f"Your final hand:{your_cards}  current score:{your_score}")
        comp_score = calculate_score(computers_cards)
        print(f"Computer's final hand:{computers_cards} current score:{comp_score}")

        if your_score > 21:
            print("You went over. You lose 😭")
        elif comp_score > 21:
            print("The computer went over. You win!")
        else:
            winner = close_21(your_score, comp_score)
            if winner == your_score:
                print("You won!")
            elif winner == comp_score:
                print("You lose")
            else:
                print("It's a draw")

    start_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if start_game != "y":
        end_of_program = True
        print("bye for now, but keep exploring")
