
def safe_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def process_coins():
    quarters = safe_int_input("How many quarters? ")
    dimes = safe_int_input("How many dimes? ")
    nickels = safe_int_input("How many nickels? ")
    pennies = safe_int_input("How many pennies? ")
    total = ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    return round(total,2) # print upto 2 decimal places



def print_report(resource, profit):
    for item, value in resource.items():
        print( f" {item.capitalize()}: {value} ")
    print(f" Money: ${profit}")