
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman (word-guessing) game in Python to practice string manipulation, control flow, and user I/O.

## 📝 Tasks

### 🛠️ Game Implementation

#### Description
Implement a playable Hangman game using the provided starter code. The program should run in the terminal and allow a single player to guess letters until they find the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined word list.
- Accept single-letter guesses from the player and reveal matching letters in the displayed word (e.g., _ a _ _ o).
- Track and display the number of remaining incorrect attempts.
- Prevent repeated guesses from unfairly counting against the player.
- End the game with a clear win or lose message and reveal the secret word.

### 🛠️ Optional Enhancements

#### Description
Add one or more extra features to improve gameplay and user experience.

#### Requirements (choose any)

- Add difficulty levels that change the number of allowed attempts.
- Display ASCII-art for the hangman that progresses with wrong guesses.
- Add a scoring or high-score feature and persist scores to a file.
- Allow replaying without restarting the program.

## 📁 Starter Code

The starter code and any assets are in the same folder: `starter-code.py`.

## ▶️ How to run

1. Ensure you have Python 3 installed.
2. From this folder, run:

```bash
python3 starter-code.py
```

## ✅ Submission

- Push your completed `starter-code.py` changes to your fork/branch.
- Include a short note in the top of the file or a separate `CHANGES.md` describing any optional enhancements you implemented.

## 💡 Hints

- Keep the game loop small and test functions individually.
- Use sets to track guessed letters for efficient membership checks.
- Validate user input to accept only single alphabetic characters.

