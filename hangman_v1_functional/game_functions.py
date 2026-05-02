def is_valid_guess(guess, guessed_letters):
    """
    Validates a user's letter guess against the game rules.

    Args:
        guess (str): The raw string input provided by the user.
        guessed_letters (list): A list of letters the user has already guessed.

    Returns:
        tuple[bool, str]: A tuple containing a boolean indicating if the guess 
                          is valid, and a string containing an error message if invalid.
    """
    if len(guess) != 1:
        return False, "You must enter exactly one character."
    
    if not guess.isalpha():
        return False, "Your guess must be a letter, no numbers or symbols."
    
    if guess in guessed_letters:
        return False, "You have already guessed this letter!"
    
    return True, ""

def guess_result(guessed_letters, chosen_word, display_word, letter_guess, lives, correct_guesses, game_won):
    """
    Evaluates a user's letter guess and updates the game state.

    Args:
        guessed_letters (list): letters the user has already tried.
        chosen_word (str): the secret word being guessed.
        display_word (list): the current board state (e.g., ['_', 'a', '_']).
        letter_guess (str): the new letter guessed by the user.
        lives (int): current remaining lives.
        correct_guesses (int): number of correctly guessed letters so far.
        game_won (bool): win status.

    Returns:
        tuple[int, int, bool]: The updated (lives, correct_guesses, game_won) state.
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
        
    return lives, correct_guesses, game_won 




            


