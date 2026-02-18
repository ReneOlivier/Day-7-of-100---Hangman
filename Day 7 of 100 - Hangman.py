# Day 7 of 100 - Hangman

import random
import hangman_art

# Print the ASCII logo from the external art module
print(hangman_art.logo)

# Small built-in word bank; extend or replace for variety
word_list = ["python", "hangman", "bicycle", "galaxy", "rhythm", "puzzle",
             "jazz", "quizzical", "xylophone", "zephyr", "vortex", "whisper"]

# Number of incorrect guesses allowed
lives = 6

# Randomly select the secret word for this session
random_word = random.choice(word_list)

# Display tracks revealed letters (use underscores for unrevealed letters).
# Initialize once to the length of the secret word to avoid growth each loop
display = ["_"] * len(random_word)

# Main game loop: continue until win or out of lives
while True:
    # Prompt the player for a single-letter guess and normalize it
    user_guess = input("Guess a letter: ").lower()

    # `display` is initialized once above; do not append underscores here.
    # This preserves revealed letters across guesses.

    # Reveal letters that match the player's guess by position
    for position in range(len(random_word)):
        if random_word[position] == user_guess:
            display[position] = user_guess

    # Incorrect guess: lose one life and show the corresponding ASCII art
    if user_guess not in random_word:
        lives -= 1
        # `hangman_art.stages` should be ordered such that index == remaining lives
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose!")
            break

    # Show current progress and remaining lives
    print(display)
    print(f"You have {lives} lives left.")

    # Win condition: if no underscores remain the player has revealed the word
    if "_" not in display:
        print("You win!")
        break