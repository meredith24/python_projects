from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_running = True

while is_running:
    user_input = input("What coffee would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_running = False

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        user_drink = menu.find_drink(user_input)

        if coffee_maker.is_resource_sufficient(user_drink) == False:
            is_running = False

        else:
            if money_machine.make_payment(user_drink.cost) == False:
                continue

            else:
                coffee_maker.make_coffee(user_drink)












