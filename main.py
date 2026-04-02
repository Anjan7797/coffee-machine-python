
from storage import load_data,save_data
from data import MENU
from machine import check_resource, check_transaction, make_coffee, refill_resources
from util import print_report, process_coins


resources, profit, history = load_data()


machine_is_on = True
while machine_is_on:
    print("\n☕ Coffee Menu")
    print("-" * 30)
    for item in MENU:
        price = MENU[item]["cost"]
        print(f"{item} (${price})")

    print("Type 'refill' or 'report' or 'history' or 'off' ")

    user_choice = input("Your choice: ").lower().strip()

    if user_choice == "off":
        print("Machine has successfully switch off.")
        machine_is_on = False

    elif user_choice == "report":
         print_report(resources, profit)

    elif user_choice == "refill":
         refill_resources(resources)
    elif user_choice == "history":
         if not history:
             print("No transaction history yet.")

         else:
             print("\n🧾 Transaction History")
             print('-' * 30 )
             for item in history:
                 print(f"{item["drink"]} - ${item["cost"]}")


    elif user_choice in MENU:
         if check_resource(user_choice, resources):
             money = process_coins()
             success, profit = check_transaction(money, MENU[user_choice]["cost"], profit) # cause it returns status, MONEY
             if success:
                 make_coffee(user_choice, resources)
                 history.append(
                     {
                         "drink" : user_choice,
                         "cost"  : MENU[user_choice]["cost"]
                     }
                 )
                 save_data(resources, profit, history)
    else:
        print("Please choose a valid option.")

