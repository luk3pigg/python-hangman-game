#Hangman Game Project
import random

#additional ideas to focus on later:
#eventually, create word banks based on different lengths of words and ask user for input on which lenght they want
#adjust number of lives: difficulty setting
#adjust times/time depending on number ie 1 is time, times is 2+


#Main lessons:
    
#Alternative to while True and return in functions, is while True and break.


#create a word bank (start with 6 letters)

word_bank = ['python', 'guitar', 'coffee', 'breeze', 'window', 'galaxy', 'jungle', 'silver', 'orchid', 'poetry']

#Initiate the first game

total_session_games = 0

def start_game():
    while True:
        start_game_response = input("Do you want to play hangman?\n YES: enter y\n NO: enter n\n").lower().strip()
        if start_game_response == 'y':
            return True
        elif start_game_response == 'n':
            return False
        else:
            print("Unfortunately, that's an an invalid input.")

game_started = start_game()

while game_started:
    print("The game is running")
    
    

    #while game_is_active:
    
    
    #select which word from word bank
    
    def select_word():
        chosen_index = random.randint(0, len(word_bank) - 1)
        return word_bank[chosen_index]
    
    chosen_word = select_word()
    print("These are the rules of the game")
    
    
    
    
    
    
    
    game_started = False
    
    
   
    

#set chosen word to python, to test
chosen_word = 'python'
lives = 6
correct_guesses = 0
guessed_letters = []
display_word = ['_'] * len(chosen_word)

def letter_validation(total_guesses):
    '''Inputs a letter guess from user and ensures both a.) it's a letter b.) it hasn't been guessed already.'''
    while True:
        letter_guess = input("\n\n\nPlease enter a letter guess: ")
        if letter_guess.isalpha() and len(letter_guess) == 1 and letter_guess not in guessed_letters:
            total_guesses += 1
            return letter_guess, total_guesses
        else:
            print("\n\n\nThat guess was invalid.")

def guess_result(letter_guess, lives, correct_guesses):
    ''' here '''
    guessed_letters.append(letter_guess)
    if letter_guess in chosen_word:
        print("\n\n\nCorrect guess!")
        correct_guesses += 1
        ocurrences = 0
        for i, letter in enumerate(chosen_word):
            if letter == letter_guess:
                ocurrences += 1
                display_word[i] = letter_guess
        print(f"Your guess appears in the secret word {ocurrences} times!")
    else:
        print("\n\n\nIncorrect guess...Unlucky!")
        lives -= 1
    return lives, correct_guesses


total_guesses = 0
while lives > 0: 
    print(f"\n\n\nYou currently have {lives} lives.")
    print(f"You currently have {correct_guesses} correct guesses.")
    if total_guesses > 0:
        print("You have guessed the following letters:")
        print(*guessed_letters)
    print("Here's what you know so far:")
    print(*display_word)
    
    letter_guess, total_guesses = letter_validation(total_guesses)
    lives, correct_guesses = guess_result(letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses)
    
        
print("Oh no! You have run out of lives!")



#main game
#display current state of word: blanks for unrevaled letters



#limited number of incorrect guesses - typically X amount

#take letter guess from user - make sure hasn't already been guessed, and must be a letter. make it lowercase

#reveal if this letter is part of word or not

#repeat process until either number of gusses used up, or word is guessed  orrectyl


#ask if user wnats to repeat the game. 


