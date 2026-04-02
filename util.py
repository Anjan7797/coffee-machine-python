


def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))
    return round(total,2) # print upto 2 decimal places


def print_report(resource, report_money):
    for item, value in resource.items():
        print( f" {item.capitalize()}: {value} ")
    print(f" Money: ${report_money}")