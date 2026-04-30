def is_valid_guess(guess, guessed_letters):
    """
    Validates the guess and returns a tuple: (is_valid_boolean, error_message)
    """
    if len(guess) != 1: #falling fast: cheapest, most protective checks go at the top! Most efficient to check this first. Check with the shortest computer power requried goes first.
        return False, "You must enter exactly one character."
    
    if not guess.isalpha():
        return False, "Your guess must be a letter, no numbers or symbols."
    
    if guess in guessed_letters:
        return False, "You have already guessed this letter!"
    
    # If it passes all checks, it's valid!
    return True, ""

def guess_result(guessed_letters, chosen_word, display_word, letter_guess, lives, correct_guesses, game_won):
    """
    Evaluates a user's letter guess and updates the game state.

    Args:
        guessed_letters (list): Letters the user has already tried.
        chosen_word (str): The secret word being guessed.
        display_word (list): The current board state (e.g., ['_', 'a', '_']).
        letter_guess (str): The new letter guessed by the user.
        lives (int): Current remaining lives.
        correct_guesses (int): Number of correctly guessed characters so far.
        game_won (bool): Current win status.

    Returns:
        tuple: Updated (lives, correct_guesses, game_won)
    """
    guessed_letters.append(letter_guess)
    
    if letter_guess in chosen_word:
        occurrences = 0
        for i, letter in enumerate(chosen_word):
            if letter == letter_guess:
                occurrences += 1
                display_word[i] = letter_guess
        correct_guesses += occurrences
        
        if correct_guesses == len(chosen_word):
            game_won = True
    else:
        lives -= 1
        
    return lives, correct_guesses, game_won #don't need to return lists such as guessed_letters - these update automatically unlike variables 




            


