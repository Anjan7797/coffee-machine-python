# ☕ Coffee Machine Simulator

This is a simple command-line coffee machine project I built while learning Python.  
It simulates how a real coffee machine works — handling resources, taking payments, and serving drinks.


## 🚀 Features

- Buy coffee (espresso, latte, cappuccino)
- Checks if enough resources are available before making a drink
- Accepts coins and calculates total amount
- Returns change if extra money is given
- Shows current resources using a report option
- Refill feature to add more water, milk, and coffee

> I also added a refill feature to make the machine more practical.


## 🛠️ Tech Used

- Python
- Functions & Modular Programming
- Dictionaries and Loops


## ▶️ How to Run

1. Make sure Python is installed
2. Run the following command (inside the project folder):

```
python main.py
```

## 📸 Sample Output
```
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: report
Water: 300 
Milk: 200 
Coffee: 100 
Money: $0
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: cappuccino
How many quarters? 50
How many dimes? 50
How many nickels? 40
How many pennies? 90
Here is $17.4 in change
Here is your cappuccino ☕. Enjoy!
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: report
Water: 50 
Milk: 100 
Coffee: 76 
Money: $3.0
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: latte
Sorry there is not enough water
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: refill
How much water to add ml? 300
How much milk to add ml? 600
How much coffee to add g? 200
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: report
Water: 350 
Milk: 700 
Coffee: 276 
Money: $3.0
☕ Coffee Machine
--------------------------------------------------

What would you like?
espresso ($1.5)
latte ($2.5)
cappuccino ($3.0)

Type 'refill' or 'report' or 'off' 
Your choice: off
Machine has successfully switch off.

```

## 📌 Note

This project was built as part of my Python learning journey.