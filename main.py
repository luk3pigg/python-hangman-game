#Hangman Game Project
import random

#additional ideas to focus on later:
#eventually, create word banks based on different lengths of words and ask user for input on which lenght they want
#adjust number of lives: difficulty setting



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

while lives > 0: 
    print(f"You currently have {lives} lives.")
    print(f"You currently have {correct_guesses} correct_guesses.")
    print("You have guessed the following letters:")
    print(*guessed_letters)
    print("Here's what you know so far:")
    print(*display_word)
    valid_guess = False
    letter_guess = input("Please enter a letter guess: ")
    if letter_guess.isalpha() and len(letter_guess) == 1:
        valid_guess = True
    else:
        print()
    
    
        
    
    
    
    
    
    
    
    break
print("Oh no! You have run out of lives!")



#main game
#display current state of word: blanks for unrevaled letters



#limited number of incorrect guesses - typically X amount

#take letter guess from user - make sure hasn't already been guessed, and must be a letter. make it lowercase

#reveal if this letter is part of word or not

#repeat process until either number of gusses used up, or word is guessed  orrectyl


#ask if user wnats to repeat the game. 


