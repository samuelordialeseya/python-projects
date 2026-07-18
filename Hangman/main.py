import random
from hangman_words import word_list
from hangman_art import stages, logo

# Print the Hangman logo
print(logo)

# Player starts with 6 lives
lives = 6

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Turn the word into a list of letters
answer = [*chosen_word]

# Create hidden word (e.g. "_____")
word_len = "_" * len(chosen_word)

# Stores the letters guessed correctly
correct_answer = set()

# Stores ALL guessed letters to prevent duplicates
guessed_letters = set()

print(word_len)
print(stages[lives])

# Keep playing while the player still has lives
while lives > 0:

    # Checks if the current guess is correct
    correct_guess = False

    # Rebuilds the displayed word every round
    display = ""

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Stop duplicate guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'.")
        print(display if display else word_len)
        print(stages[lives])
        continue

    # Save this guess
    guessed_letters.add(guess)

    # Go through every letter in the answer
    for letter in answer:

        # If we already guessed this letter before, show it
        if letter in correct_answer:
            display += letter

        # If the current guess matches this letter
        elif letter == guess:
            correct_answer.add(guess)   # Remember the correct letter
            display += guess
            correct_guess = True

        # Otherwise, keep it hidden
        else:
            display += "_"

    # Wrong guess → lose a life
    if not correct_guess:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    # Correct guess
    else:
        print("Correct Guess!")

    # Show updated word and hangman
    print(display)
    print(stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    # If no more underscores, player wins
    if display == chosen_word:
        print("🎉 YOU WIN!")
        break

# Ran out of lives
if lives == 0:
    print(f"IT WAS '{chosen_word.upper()}'! YOU LOSE.")