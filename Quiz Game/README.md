# Quiz Game

**Date Finished:** August 19, 2026

This is my implementation of the True/False Quiz Game.

## What I Made
I built a Python quiz program that reads a list of questions, presents them one at a time, and checks the user's answer against the correct result. The program tracks the question number, keeps score, and prints a final summary when the quiz ends.

## What I Learned 

I learned a few important lessons about structure, logic, and keeping track of game state:

1. **Using a Quiz Class to Organize Logic:**
   In my project, I learned that putting the quiz logic into a `QuizBrain` class makes the code easier to follow. The class controls the question count, score, and answer checking, instead of having everything spread across multiple loose variables.

2. **Tracking Game State Correctly:**
   I had to make sure the score and question number updated in the correct places. If I changed the score before checking the answer or counted the wrong question number, the final result would be inaccurate. This taught me how important it is to manage state carefully in loops and methods.

3. **Separating Data from Behavior:**
   I learned to keep the question bank in one place and use objects to represent each question. This made the program cleaner and easier to expand. Instead of hardcoding every question into the main flow, I stored them in a list and used a class to handle the logic for each question.

Overall, this project helped me understand how classes can make a program more organized and easier to manage. It also reinforced the idea that a good game or app depends on clear state tracking and clean separation between data and logic.
