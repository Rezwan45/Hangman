import random

def hangman_game():
    # Word list
    word_list = ["monkey", "baboon", "camel"]

    # Hangman ASCII art for each life count
    hangman_stages = [
        """
           ----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        """,
        """
           ----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        """,
        """
           ----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        """,
        """
           ----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           ----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           ----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           ----
           |   |
               |
               |
               |
               |
        --------
        """
    ]

    # Randomly choose a word
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # Initialize game variables
    blanks = ["_"] * word_length  # Display blanks for the word
    lives = 6  # Number of lives
    guessed_letters = []  # Store guessed letters

    print("Welcome to Hangman!")
    print(" ".join(blanks))

    # Main game loop
    while lives > 0 and "_" in blanks:
        # Prompt the user for a guess
        guess = input("Guess a letter: ").lower()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
            for index in range(word_length):
                if chosen_word[index] == guess:
                    blanks[index] = guess
        else:
            lives -= 1
            print(f"Wrong guess! You lost a life. Lives remaining: {lives}")
            print(hangman_stages[6 - lives])

        # Display the current state of the word
        print(" ".join(blanks))

    # End of game
    if "_" not in blanks:
        print(f"Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"You lost! The word was: {chosen_word}")

# Start the game
if __name__ == "__main__":
    hangman_game()
