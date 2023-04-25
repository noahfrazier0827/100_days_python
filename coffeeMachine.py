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

while True:
    drink_selection = input("What would you like? (espresso/latte/cappuccino):\n")

    # check resources for the drink
    
    if drink_selection == "espresso" or drink_selection == "latte" or drink_selection == "cappuccino":
        for ingredient in MENU[drink_selection]["ingredients"]:
            if resources[ingredient] < MENU[drink_selection]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}.")

        # process the money

        print(f"the {drink_selection} will be {MENU[drink_selection]['cost']}")
        userDollar = float(input("How many dollars will you insert?\n"))
        userQuarter = float(input("How mant quarters will you insert?\n"))
        userQuarterCalc = userQuarter * 0.25
        userMoney = userDollar + userQuarterCalc

        # check if the money is enough, otherwise refund the money
        while True:
            moneyReq = float(MENU[drink_selection]['cost'])
            if moneyReq > userMoney:
                print("Sorry, you don't have enough money.")
                print(f"{userMoney} was refunded back to you.")
                break

            # deduct ingredients, if transaction success, make drink

            if moneyReq <= userMoney:
                for ingredient in MENU[drink_selection]["ingredients"]:
                    resources[ingredient] -= MENU[drink_selection]["ingredients"][ingredient]
                print(f"Enjoy your {drink_selection}!")
                change = userMoney - moneyReq
                print(f"{change} is your change back.")
                break

    elif drink_selection == "report":
        print(resources)

    elif drink_selection == "off":
        break

    else:
        print("select a valid option.")


