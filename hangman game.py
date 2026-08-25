
def play_hangman():
    words = "python"
    secret_word = words
    
    # Track guessed letters and allowed incorrect attempts
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
    
        current_progress = " ".join(display_word)
        print("Word:",current_progress)
        
        if "_" not in display_word:
            print(" Congratulations! You won! ")
            return

        
        guess = input("Guess a letter: ").lower().strip()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Remaining incorrect guesses: {remaining}")

    # Lose condition
    print(f"\nGame Over! You ran out of guesses. The word was '{secret_word}'.")



play_hangman()