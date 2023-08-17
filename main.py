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
    "money": 0,
}


# Ask user for an input.
def prompt_user():
    while True:
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if answer == "espresso" or answer == "latte" or answer == "cappuccino" or answer == "off" or answer == "report":
            break
    return answer


# Print report of all resources if user asks.
def print_report():
    for resource in resources:
        amount = resources[resource]
        if resource == "money":
            amount = f"${'{0:.2f}'.format(amount)}"
        elif resource == "coffee":
            amount = f"{amount}g"
        else:
            amount = f"{amount}ml"

        print(f"{resource.capitalize()}: {amount}")


# Check if the machine has enough resources to make what the user needs.
def check_resources(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if resources[ingredient] < coffee_ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


# Charge user the right cost in coins if they buy a coffee. Give change if needed. Refund money if not enough.
def get_coins(cost):
    print(f"One espresso will be ${'{0:.2f}'.format(cost)}")
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = (quarters*.25) + (dimes*.10) + (nickles*.05) + (pennies*.01)

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = total - cost
        print(f"Here is ${'{0:.2f}'.format(change)} in change.")

    resources["money"] += cost
    return True


# Make the coffee. Take away resources accordingly.
def make_coffee(coffee_name):
    coffee_type = MENU[coffee_name]
    coffee_ingredients = coffee_type["ingredients"]

    if check_resources(coffee_ingredients):
        cost = coffee_type["cost"]
        if get_coins(cost):
            for ingredient in coffee_ingredients:
                resources[ingredient] -= coffee_ingredients[ingredient]
            print(f"Here is your {coffee_name}. Enjoy!")


# Start coffee machine.
def start():
    while True:
        answer = prompt_user()

        if answer == "off":
            break
        elif answer == "report":
            print_report()
        else:
            make_coffee(answer)


start()
