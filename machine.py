
from data import MENU
from util import safe_int_input



def check_resource(drink, resources):
    """Check if there are enough resources to make the selected drink.

    Args:
        drink (str): Name of the drink.
        resources (dict): Available resources in the machine.

    Returns:
        bool: True if resources are sufficient, otherwise False.
    """
    # This pulls both key and value out of the nested dictionary at once
    for item, quantity in MENU[drink]["ingredients"].items():
            
            if quantity > resources.get(item,0):
                print(f"Sorry there is not enough {item}")
                return False
    return True




def check_transaction(money_received, drink_cost, profit):
    """Process the payment and update profit if transaction is successful.

    Args:
        money_received (float): Money inserted by the user.
        drink_cost (float): Cost of the selected drink.
        profit (float): Current total profit.

    Returns:
        tuple: (bool, float) → transaction status and updated profit.
    """
    
    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False, profit

    else:
        profit += drink_cost
        if drink_cost < money_received:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change")

    return True, profit




def make_coffee(drink, resources):
    """Deduct ingredients from resources and serve the selected drink.

    Args:
        drink (str): Name of the drink.
        resources (dict): Available resources in the machine.
    """
    
    for item, quantity in MENU[drink]["ingredients"].items():
        resources[item] -= quantity
    print(f"Here is your {drink} ☕. Enjoy!")



def refill_resources(resources):
    """Refill machine resources based on user input.

    Args:
        resources (dict): Available resources in the machine.
    """
    
    units = {
         "water" : "ml",
         "milk"  : "ml",
        "coffee" : "g",
    }
    for item in resources:
        
        unit = units.get(item, "units")
        amount = safe_int_input(f"How much {item} to add ({unit})? ")
        resources[item] += amount
