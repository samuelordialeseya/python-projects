# Silent Auction

This is my implementation of the Blind (Silent) Auction program.

## What I Made
I built a Python program that takes bids from different users secretly by clearing the console after each entry. Once all the bidders have entered their name and bid amount, the program determines the winner with the highest bid.

## What I Learned (Comparing my code to Angela Yu's)

By comparing my code with Angela Yu's, I learned a few important lessons about logic and code structure:

1. **Calculating the Highest Bid at the End:** 
   In my code, I placed the loop that finds the highest bidder *inside* the `while` loop. This means the program recalculates the highest bid every time a new user enters a bid. Angela's code, on the other hand, waits until the `while` loop is completely finished, and *then* calculates the highest bid just once. This is more efficient!

2. **Using Functions to Organize Code:**
   Angela encapsulated the logic for finding the highest bidder into its own function `find_highest_bidder(bidding_record)`. This makes the code much cleaner, easier to read, and reusable.

3. **Updating the Correct Variables:**
   In my code for checking the highest bid:
   ```python
   if bid_amount > highest_bid:
       most_value = bid_amount
       winner = bidder
   ```
   I assigned the new highest amount to `most_value`, but I forgot to update the actual `highest_bid` variable! Because `highest_bid` stays `0`, the final print statement will show the winning bid as `$0`, and it will just declare the last person as the winner (since any bid is > 0). Angela's code correctly updates the highest bid tracking variable: `highest_bid = bid_amount`.

Overall, this project taught me the importance of variable tracking and how structuring logic outside of data-collection loops can make a program much more efficient and clean!
