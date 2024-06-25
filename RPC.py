import random

# Define hand images and winning conditions using a dictionary
hand_images = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

winning_conditions = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}

# Get user input and handle invalid choices
user_choice_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
valid_choices = range(len(hand_images))  # Create a range for valid choices
if user_choice_index not in valid_choices:
    print("Invalid choice. Please enter 0, 1, or 2.")
    exit()

user_choice = list(hand_images.keys())[user_choice_index]  # Get the user's choice as a string

# Generate computer's choice randomly
computer_choice_index = random.randint(0, len(hand_images) - 1)
computer_choice = list(hand_images.keys())[computer_choice_index]

# Print user and computer choices
print("You chose:")
print(hand_images[user_choice])
print("Computer chose:")
print(hand_images[computer_choice])

# Determine winner using dictionary lookup and conditionals
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice in winning_conditions[computer_choice]:
    print("You lose!")
else:
    print("You win!")