
import data
from machine import check_resource, check_transaction, make_coffee, refill_resources
from util import print_report, process_coins



machine_is_on = True
while machine_is_on:
    print(f"☕ Coffee Machine\n {'-' * 50}")
    print("""
What would you like?
espresso($1.5)
latte($2.5)
cappuccino($3.0)
""")

    print("Type 'refill' or 'report' or 'off' ")

    user_choice = input("Your choice: ").lower().strip()

    if user_choice == "off":
        print("Machine has successfully switch off.")
        machine_is_on = False

    elif user_choice == "report":
         print_report(data.resources, data.MONEY)

    elif user_choice in data.MENU:
         if check_resource(user_choice):
             money = process_coins()
             if check_transaction(money, data.MENU[user_choice]["cost"]):
                 make_coffee(user_choice)
    elif user_choice == "refill":
         refill_resources()
    else:
        print("Please choose an valid option.")
