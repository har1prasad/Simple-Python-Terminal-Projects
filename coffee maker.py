MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${profit}
    """)

def check_resources(input):
    order_ingredients = MENU[input]["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    try:
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return 0
    return total

def check_price(price, input):
    cost = MENU[input]["cost"]
    if cost <= price:
        change = round(price - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(input):
    order_ingredients = MENU[input]["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {input} ☕️. Enjoy!")

end_of_program = False
while not end_of_program:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("The System is shutting down for maintenance......")
        end_of_program = True
    elif user_choice == "report":
        report()
    else:
        if user_choice in MENU:
            if check_resources(user_choice):
                total = process_coins()
                if total > 0 and check_price(total, user_choice):
                    make_coffee(user_choice)
            else:
                continue
        else:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")
            continue
