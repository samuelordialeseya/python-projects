from logging import log
import art

print(art.logo)

continue_auction = True
winner = ""
highest_bid = 0
auction = {}

 # TODO-1: Ask the user for input
while continue_auction:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    # TODO-2: Save data into dictionary {name: price}
    auction[name] = bid

    # TODO-3: Whether if new bids need to be added
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if choice == "yes":
        print("\n" * 20)

    else:
        continue_auction = False

    # TODO-4: Compare bids in dictionary
    for bidder in auction:
        bid_amount = auction[bidder]

        if bid_amount > highest_bid:
            most_value = bid_amount
            winner = bidder
        else:
            continue



print(f"The winner is {winner} with a bid of ${highest_bid}")











