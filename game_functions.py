import random

def start_game():
    '''starts the game based on user input'''
    start_game_response = input("Welcome! Are you ready to play hangman?\nYES: enter y\nNO: enter n\n\n").lower().strip()
    while True:
        if start_game_response == 'y':
            return True
        elif start_game_response == 'n':
            print("\nOh, never mind. Have a nice day!")
            return False
        else:
            start_game_response = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()


def select_word(word_bank):
    '''Selects a word at random from the word bank'''
    chosen_index = random.randint(0, len(word_bank) - 1)
    return word_bank[chosen_index]


def letter_validation(total_guesses, guessed_letters):
    '''Inputs a letter guess from user and ensures both a.) it's a letter b.) it hasn't been guessed already.'''
    while True:
        letter_guess = input("\n\n\nPlease enter a letter guess: ")
        if letter_guess.isalpha() and len(letter_guess) == 1 and letter_guess not in guessed_letters:
            total_guesses += 1
            return letter_guess, total_guesses
        else:
            print("\n\n\nThat guess was invalid. Ensure the guess is a single letter that hasn't already been guessed!")


def guess_result(guessed_letters, chosen_word, display_word, letter_guess, lives, correct_guesses, game_won):
    '''Adds guess to guessed letters list, determines if guess is correct, and updates lives accordingly '''
    guessed_letters.append(letter_guess)
    if letter_guess in chosen_word:
        ocurrences = 0
        for i, letter in enumerate(chosen_word):
            if letter == letter_guess:
                ocurrences += 1
                display_word[i] = letter_guess
        correct_guesses += ocurrences
        print("\n\n")
        print(*display_word)
        if correct_guesses == len(chosen_word):
            game_won = True
        else:
            print("\n\n\nCorrect guess!")
            print(f"Your guess appears in the secret word {ocurrences} times!")
    else:
        print("\n\n\nIncorrect guess...Unlucky!")
        lives -= 1
    return lives, correct_guesses, game_won


def restart_game():
    '''restarts the game based on user input'''
    restart_game_response = input("Do you want to play another game?\n YES: enter y\n NO: enter n\n\n").lower().strip()
    while True:
        if restart_game_response == 'y':
            return True
        elif restart_game_response == 'n':
            print("\nOh, never mind. Have a nice day!")
            return False
        else:
            restart_game_response = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()
            


