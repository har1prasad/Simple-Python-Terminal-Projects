# Flag to indicate whether the program should continue running
end_of_program = False

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract the second number from the first
def sub(n1, n2):
    return n1 - n2

# Function to divide the first number by the second
def div(n1, n2):
    return n1 / n2

# Function to multiply two numbers
def mul(n1, n2):
    return n1 * n2

# Prompt user for the first number
first_number = int(input("Enter the first number: "))

while not end_of_program:
    # Dictionary to map operator symbols to corresponding functions
    operator_functions = {
        "+": add,
        "-": sub,
        "/": div,
        "*": mul
    }

    # Display available operators
    for operator in operator_functions:
        print(operator)

    # Prompt user to choose an operator
    chosen_operator = input("Enter the operator ['+', '-', '*', '/']: ")

    # Prompt user for the second number
    second_number = int(input("Enter the second number: "))

    # Get the function corresponding to the chosen operator
    operation_function = operator_functions[chosen_operator]

    # Perform the calculation
    result = operation_function(first_number, second_number)
    print(f"{first_number} {chosen_operator} {second_number} = {result}")

    # Flag to control the continuation choice loop
    end_of_choice = False
    while not end_of_choice:
        # Ask the user if they want to continue
        continue_choice = input("Do you want to continue calculation 'Y' or 'N': ").lower()
        if continue_choice == "y":
            # If yes, set the first number to the result and continue
            first_number = result
            end_of_program = False
            end_of_choice = True
        elif continue_choice == "n":
            # If no, end the program
            end_of_program = True
            end_of_choice = True
        else:
            # If invalid input, prompt again
            print("Invalid choice")
            end_of_choice = False
