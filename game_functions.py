import random

def parse_yes_no(response):
    """
    Evaluates a yes/no string.
    Returns True for 'y', False for 'n', and None for invalid inputs.
    """
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        return None

def ask_yes_no(prompt):
    """
    Asks the user a yes/no question based on the provided prompt.
    Returns True if 'y', False if 'n'.
    """
    while True:
        response = input(f"{prompt}\nYES: enter y\nNO: enter n\n\n").lower().strip()
        if response == 'y':
            return True
        elif response == 'n':
            print("\nGot it. Have a nice day!")
            return False
        else:
            print("\nUnfortunately, that's an invalid input. Please try again.")

def select_word(word_list):
    '''Selects a word at random from the provided list'''
    return random.choice(word_list) #built in function to randomly select from list

def is_valid_guess(guess, guessed_letters):
    """
    Checks if the user's guess is exactly one letter and hasn't been guessed yet.
    Returns True if valid, False otherwise.
    """
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters #for this to return True, all 3 conditions must be True

def guess_result(guessed_letters, chosen_word, display_word, letter_guess, lives, correct_guesses, game_won):
    '''Updates game state based on the guess.'''
    guessed_letters.append(letter_guess)
    
    if letter_guess in chosen_word:
        ocurrences = 0
        for i, letter in enumerate(chosen_word):
            if letter == letter_guess:
                ocurrences += 1
                display_word[i] = letter_guess
        correct_guesses += ocurrences
        
        if correct_guesses == len(chosen_word):
            game_won = True
    else:
        lives -= 1
        
    return lives, correct_guesses, game_won




            


