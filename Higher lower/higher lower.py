import art as ar # type: ignore
import gamedata as g # type: ignore
import random
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def random_value(data):
    ran = random.randint(0,49)
    return data[ran]

def check(a,b):
    if (a["follower_count"] > b["follower_count"]):
        return "a"
    elif(a["follower_count"] < b["follower_count"]):
        return "b"
    else:
        return None
      
current_score = 0
end_of_program = False
a = random_value(g.data)

print(ar.logo)
    
while not end_of_program:
    print(f"Compare A : {a["name"]} a {a["description"]} from {a["country"]}")

    print(ar.vs)

    b = random_value(g.data)
    print(f"Against B : {b["name"]} a {b["description"]} from {b["country"]}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()


    if(check(a,b) == user_input):
        current_score += 1
        if (user_input == "b"):
            a = b
        clear_screen()
        print(ar.logo)
        print(f"You're right! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        end_of_program = True
        