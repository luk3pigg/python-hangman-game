import random

def start_game():
    '''starts the game based on user input'''
    start_game_response = input("Welcome! Are you ready to play hangman?\nYES: enter y\nNO: enter n\n\n").lower().strip()
    while True: #loops so if input is not y or n, this question is repated
        if start_game_response == 'y':
            return True #loop breaks
        elif start_game_response == 'n':
            print("\nOh, never mind. Have a nice day!")
            return False #loop breaks, main.py just ends 
        else:
            start_game_response = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()


def select_word(word_bank):
    '''Selects a word at random from the word bank'''
    chosen_index = random.randint(0, len(word_bank) - 1) #uses length of list from dictionary word_bank in main.py
    return word_bank[chosen_index]


def letter_validation(total_guesses, guessed_letters):
    '''Inputs a letter guess from user and ensures both a.) it's a letter b.) it hasn't been guessed already.'''
    while True: #loops so command is asked again if invalid input
        letter_guess = input("\n\n\nPlease enter a letter guess: ")
        if letter_guess.isalpha() and len(letter_guess) == 1 and letter_guess not in guessed_letters: #ensures letter guess is a letter not a number, and only one letter
            total_guesses += 1
            return letter_guess, total_guesses #breaks loop
        else:
            print("\n\n\nThat guess was invalid. Ensure the guess is a single letter that hasn't already been guessed!") #ensures letter has not already been guessed


def guess_result(guessed_letters, chosen_word, display_word, letter_guess, lives, correct_guesses, game_won):
    '''Adds guess to guessed letters list, determines if guess is correct, and updates lives accordingly '''
    guessed_letters.append(letter_guess) #adds guessed letter to list
    if letter_guess in chosen_word:
        ocurrences = 0
        for i, letter in enumerate(chosen_word):
            if letter == letter_guess:
                ocurrences += 1
                display_word[i] = letter_guess #changes _ into the letter
        correct_guesses += ocurrences #updates correct guesses
        print("\n\n")
        print(*display_word) #unpacks the list of letters and _ 
        if correct_guesses == len(chosen_word):
            game_won = True #game ends as all letters have been correctly guessed
        else:
            print("\n\n\nCorrect guess!")
            print(f"Your guess appears in the secret word {ocurrences} times!") #game does not end, game_won remains False 
    else:
        print("\n\n\nIncorrect guess...Unlucky!")
        lives -= 1
    return lives, correct_guesses, game_won


def restart_game():
    '''restarts the game based on user input'''
    restart_game_response = input("Do you want to play again?\nYES: enter y\nNO: enter n\n\n").lower().strip()
    while True:
        if restart_game_response == 'y':
            return True
        elif restart_game_response == 'n':
            print("\nOh, never mind. Have a nice day!")
            return False
        else:
            restart_game_response = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()
            


