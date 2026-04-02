
import data



def check_resource(drink):
    # This pulls both key and value out of the nested dictionary at once
    for item, quantity in data.MENU[drink]["ingredients"].items():
            #Using .get() (The Safe Way) Result: None (No crash!) if key not found
            if quantity > data.resources.get(item,0):
                print(f"Sorry there is not enough {item}")
                return False
    return True


def check_transaction(money_received, drink_cost):

    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False

    else:
        data.MONEY += drink_cost
        if drink_cost < money_received:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change")

    return True

def make_coffee(drink):
    for item, quantity in data.MENU[drink]["ingredients"].items():
        data.resources[item] -= quantity
    print(f"Here is your {drink} ☕. Enjoy!")


def refill_resources():
    units = {
         "water" : "ml",
         "milk"  : "ml",
        "coffee" : "g",
    }
    for item in data.resources:
        # ensures that if you add a resource but forget to add its unit, the program won't crash—it will just say "(units)".
        unit = units.get(item, "units")
        amount = int(input(f"How much {item} to add {unit}? "))
        data.resources[item] += amount