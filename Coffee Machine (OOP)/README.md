# Coffee Machine (OOP)

**Date Finished:** August 8, 2026

This is my implementation of the Object-Oriented Programming (OOP) Coffee Machine program.

## What I Made
I built a Python program that simulates a digital coffee machine using multiple external classes (`Menu`, `CoffeeMaker`, and `MoneyMachine`). The program prompts users for a drink selection, dynamically checks if there are enough ingredients left, processes coin payments sequentially, calculates accurate change, and updates its internal resource logs after every successful transaction.

## What I Learned (Comparing my code to Angela Yu's)

I learned a few important lessons about logic refinement, object interactions, and debugging:

1. **Leveraging Return Values Over Hardcoded Logic:**
   In my initial code, I wrote separate `if/elif` blocks for every individual drink option (espresso, latte, cappuccino). By studying the project requirements and structural guidelines, I learned that `menu.find_drink(choice)` dynamically handles the text input. If the drink doesn't exist, it returns `None`. Checking `if order is not None:` allowed me to handle all flavors in a single block of code, removing massive amounts of redundant logic.

2. **Differentiating Raw Input vs. Class Objects:**
   I ran into an `AttributeError` because I was passing a raw text string (`choice`) to a method that expected a complex custom class object (`order`). I learned how to read tracebacks from the bottom up to pinpoint exactly when a variable turns into a string or a object, and how to use dot notation (like `order.cost`) to pull attributes directly out of an object.

3. **Separating Machine Commands from Menu Items:**
   I initially placed the `order` conversion logic at the very top of my loop, which broke secret system commands like `"off"` and `"report"` because they are not on the coffee menu. I learned to structure my control flow so that the program checks the raw `choice` string for maintenance commands *before* it tries to parse the input into a menu item.

Overall, this project shifted my mindset from manual, hardcoded scripts to utilizing existing classes efficiently. It taught me how to read complex crash logs and let objects do the heavy lifting.
