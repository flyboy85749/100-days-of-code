MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item} for you order. Please try something else.")
            return False
    return True


def count_coins():
    total = int(input("How many quarters did you put in my coin slot? ")) * 0.25
    total += int(input("How many dimes did you put in my coin slot? ")) * 0.10
    total += int(input("How many nickels did you put in my coin slot? ")) * 0.05
    total += int(input("How many pennies did you put in my coin slot? ")) * 0.01
    return total


def successful_transaction(coins_received, drink_price):
    if coins_received >= drink_price:
        change = round(coins_received - drink_price, 2)
        print(f"You gave me ${coins_received}. The total cost is ${drink_price}. Your change is ${change}")
        global profit
        profit += drink_price
        return True
    else:
        print(f"Sorry, that is not enough money. I have refunded you the ${coins_received}.")
        return False
