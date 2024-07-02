from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffeemaker = CoffeeMaker()
Moneymachine = MoneyMachine()
menus = Menu()

end_of_program = False

while not end_of_program:
    user_input = input(f"What would you like? {menus.get_items()} :").lower()
    if user_input == "off":
        print("The System is shutting down for maintenance......")
        end_of_program = True
    elif user_input == "report":
        Coffeemaker.report()
        Moneymachine.report()
        continue
    else:
        menuitems = menus.find_drink(user_input)
        if menuitems is None:
            continue
        else:
            resources = Coffeemaker.is_resource_sufficient(menuitems)
            if not resources:
                continue
            else:
                money = Moneymachine.make_payment(menuitems.cost)
                if money:
                    Coffeemaker.make_coffee(menuitems)
                else:
                    continue