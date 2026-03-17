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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coin():
    quarters = 0.25 * int(input("How many quarters? "))
    dimes = 0.10 * int(input("How many dimes? "))
    nickels = 0.05 * int(input("How many nickles? "))
    pennies = 0.01 * int(input("How many pennies? "))
    total_money = quarters + dimes + nickels + pennies
    return total_money



profit = 0

is_working = True
while is_working == True:
    coins = 0
    user_choice = str(input("What would you like? (espresso, latte, cappuccino): "))
    if user_choice == "off":
        is_working = False

    elif user_choice == "off":
        is_working = False

    elif user_choice == "report":
        print("water:", resources["water"])
        print("milk:", resources["milk"])
        print("coffee:", resources["coffee"])
        print("profit:", profit)

    elif user_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            break

        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            break



        coins = process_coin()

        if coins < MENU["espresso"]["cost"]:
            print("Sorry there is not enough money. Money refunded.")
            continue

        if coins >= MENU["espresso"]["cost"]:
            change = float(coins - MENU["espresso"]["cost"])
            profit += MENU["espresso"]["cost"]
            print(f"here is ${change:.2f} dollars in change.")
            print("Enjoy your espresso!")


        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]




    elif user_choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            break

        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            break

        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            break

        coins = process_coin()

        if coins < MENU["latte"]["cost"]:
            print("Sorry there is not enough money. Money refunded.")
            continue

        if coins >= MENU["latte"]["cost"]:
            change = float(coins - MENU["latte"]["cost"])
            profit += MENU["latte"]["cost"]
            print(f"here is ${change:.2f} dollars in change.")
            print("Enjoy your latte!")


        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]



    elif user_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            break

        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            break

        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            break

        coins = process_coin()

        if coins < MENU["cappuccino"]["cost"]:
            print("Sorry there is not enough money. Money refunded.")
            continue

        if coins >= MENU["cappuccino"]["cost"]:
            change = float(coins - MENU["latte"]["cost"])
            profit += MENU["latte"]["cost"]
            print(f"here is ${change:.2f} dollars in change.")
            print("Enjoy your cappuccino!")

        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]














