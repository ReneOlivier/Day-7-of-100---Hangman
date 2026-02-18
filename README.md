# Hangman (Day 7 of 100 Days of Code)

**Overview**

This is a simple command-line Hangman game built as part of the "100 Days of Code" course by Angela Yu. The program selects a secret word and lets the player guess letters until they either find the word or run out of lives. The project demonstrates basic Python programming concepts and a small separation between code and ASCII art assets.

**How to run**

- Make sure you have Python 3 installed.
- From the project directory run:

```bash
python "Day 7 of 100 - Hangman.py"
```

Follow the on-screen prompts to guess letters.

**Files**

- `Day 7 of 100 - Hangman.py` — main game script that handles game logic and user interaction.
- `hangman_art.py` — ASCII art assets used by the game (hangman stages and logo).

**Skills Learned**

- Python basics: variables, control flow (if/else), loops (`for`, `while`).
- Working with strings and lists for word/letter handling.
- Using the `random` module to select a secret word.
- Basic input/output for command-line interaction.
- Structuring a small project across multiple files (separating art from logic).
- Simple game logic design: tracking guessed letters, lives, and win/loss conditions.
- Debugging and incremental development (testing game flow and edge cases).

**Notes & Next Steps**

- You can extend the game by adding a larger word list, saving high scores, or adding difficulty levels.
- For visual polish, consider enhancing `hangman_art.py` or adding colored output via a package like `colorama`.

---

