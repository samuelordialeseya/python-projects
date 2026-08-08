from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
cashier = MoneyMachine()
for_sale = menu.get_items()
machine_on = True

while machine_on:
    # Requirement 1: Prompt the user
    choice = input(f"What would you like? ({for_sale}): ")

    # Requirement 2: Turn off the machine
    if choice == "off":
        machine_on = False
    
    # Requirement 3: Print resource report
    elif choice == "report":
        coffeemaker.report()
        cashier.report()
        
    else:
        # Check if user typed a valid drink from the menu
        order = menu.find_drink(choice)
        
        if order is not None:
            # Requirement 4: Check if resources are sufficient
            availability = coffeemaker.is_resource_sufficient(order)

            if availability:
                # Requirements 5 & 6: Process coins and check if payment is successful
                payment_successful = cashier.make_payment(order.cost)
                
                if payment_successful:
                    # Requirement 7: Deduct resources and serve the coffee
                    coffeemaker.make_coffee(order)
        else:
            # Handle actual invalid entries (typos)
            print("Invalid entry, try again.")
