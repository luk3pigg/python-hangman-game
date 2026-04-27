import game_functions as gf
import time
import statistics

#constants and settings

word_bank = {5: ['queue', 'knack', 'odour', 'glyph', 'fjord', 'hyena', 'dwarf', 'stiff', 'jazzy', 'quick'], 6: ['python', 'guitar', 'coffee', 'breeze', 'window', 'galaxy', 'jungle', 'silver', 'orchid', 'poetry'], 7: ['pyjamas', 'chimney', 'whiskey', 'draught', 'defence', 'offence', 'license', 'chevron', 'acquire'], 8: ['dialysis', 'strength', 'practise', 'mountain', 'skeleton', 'flamingo', 'backpack', 'syndrome', 'keyboard', 'question'], 9: ['programme', 'neighbour', 'aluminium', 'travelled', 'authorise', 'organised', 'chocolate', 'scavenger', 'broadcast', 'average'], 10: ['specialise', 'organising', 'recognised', 'everything', 'journalism', 'playground', 'challenged', 'background', 'motivation', 'excellence']}

#UI helper functions

def get_yes_no_input(prompt):
    """
    Handles the UI loop for asking the user a yes/no question.
    Relies on game_functions to parse the logic.
    """
    while True:
        user_input = input(f"{prompt}\nYES: enter y\nNO: enter n\n\n").lower().strip()
        is_ready = gf.parse_yes_no(user_input)
        
        if is_ready is True:
            return True
        elif is_ready is False:
            print("\nGot it. Have a nice day!")
            return False
        else:
            print("\nUnfortunately, that's an invalid input. Please try again.")

#main game engine

def main(): #master function protects global variables by transforming into local variables
    #global counter stats
    total_session_games = 0 
    total_wins = 0
    winning_times = []
    
    
                   
    game_active = get_yes_no_input("Welcome! Are you ready to play hangman?") #Initialisation of game
    game_start = time.time() #overall timer starts
    first_cycle = True #first cycle is different - asks for rules etc 
    while game_active:   #loop for each session
        while first_cycle: #this inner loop only runs for the first cycle
            
        
        rules = input("Would you like to know the rules before we begin?\nYES: enter y\nNO: enter n\n\n")
            while True:
                if rules == 'y':
                    print("These are the rules.\nOBJECTIVE: guess the secret word by guessing the letters it contains!\nYou will choose how many lives you have, and the length of the secret word.\nIf your letter guess is in the secret word, its location/s in the secret word will be revealed!\nBut be careful: if your letter guess is not in the secret word, you will lose a life.\nYou win the game if you guess all the letters and hence the word without losing all your lives!\n\nSo, without further ado....\n\n")
                    first_cycle = False #first cycle message above is not repeated 
                    break
                elif rules == 'n':
                    print("Cool.")
                    first_cycle = False
                    break
                else:
                    rules = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()
                    
                    
       rules = get_yes_no_input("Would you like to know the rules before we begin?")         
        
        
        while True: #will loop around until correct input is inputted
            try:
                word_length = int(input("Please select how many letters you would like the secret word to have, between 5 and 10."))
                if 5 <= word_length <= 10:
                    break #this word_length is fine, loop exited, program continues 
                else:
                    print("You have selected an invalid number of letters.")
            except ValueError:
                print("You have selected an invalid number of letters.") # says this regardless of whether the input is not in range 5-10, or if a letter or different character is inputted
                
        chosen_word = gf.select_word(word_list = word_bank[word_length]) #accesses dictionary with key=word length and uses function in other file
        
        
        
        while True:
            try:
                lives = int(input("Please select how many lives you would like, between 5 and 10."))
                if 5 <= lives <= 10:
                    break
                else:
                    print("You have selected an invalid number of lives.")
            except ValueError:
                print("You have selected an invalid number of lives.")
                #same logic as above but now for lives 
        
        
        
        #Initialisation of each individual game
        correct_guesses = 0
        guessed_letters = []
        display_word = ['_'] * len(chosen_word)
        total_guesses = 0
        game_won = False
        start_time = time.time() #starts time for individual game
        while lives > 0 and not game_won: #loop for each individual game. For this loop to run, both have to be true: lives >0 AND game has not been won ie correct guesses = length of word 
            if total_guesses == 0: #messages just for the first guess e.g. game has started 
                print("\nThe timer is on!")
                print("\nThis is your first guess!")
                print(f"\nYou currently have {lives} lives.")
                print("\nThis is the secret word:")
                print(*display_word)
            else:
                print("\n20 seconds have gone so far!") #update this error
                print(f"\nThis is guess number {total_guesses + 1}.")
                print(f"\nYou currently have {lives} lives.")
                print(f"\nYou currently have {correct_guesses} correct guesses.")
                print("\nYou have guessed the following letters:")
                print(*guessed_letters)
                print("\nHere's what you know so far:")
                print(*display_word)
            
            while True:
                letter_guess = input("\n\n\nPlease enter a letter guess: ").lower().strip()
                if gf.is_valid_guess(letter_guess, guessed_letters): #verifies if guess is valid (meets all 3 conditions)
                    total_guesses += 1
                    break #exits loop
                else:
                    print("\n\n\nThat guess was invalid. Ensure the guess is a single letter that hasn't already been guessed!")
            
            
            
            lives, correct_guesses, game_won = gf.guess_result(guessed_letters, chosen_word, display_word, letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses, game_won=game_won) #updates whether the game has been won yet or not, and whether all lives have been used up yet or not - these 2 factors decide if the game has ended or not. 
            if letter_guess in chosen_word:
                occurrences = chosen_word.count(letter_guess)
                print("\n\n\nCorrect guess!")
                print(f"Your guess appears in the secret word {occurrences} times!")
            else:
                print("\n\n\nIncorrect guess...Unlucky!")
        
            
        
        if game_won: #only runs when correct guesses = number of letters in the word 
            end_time = time.time() #ends the individual game time 
            time_elapsed = round(end_time - start_time, -1) #calculates total individual game time
            winning_times.append(time_elapsed)
            average_time = round(statistics.mean(winning_times), 2)
            total_wins += 1
            print(f"\n\nYou won! The secret word was {chosen_word}!")
            print(f"You took {time_elapsed} seconds.")
            if time_elapsed == min(winning_times) and len(winning_times) > 1:
                print("WOW! That's your fastest winning time yet!")
            print(f"Your average winning time is {average_time}!")
            #win percentage
            #average time taken for the wins
        else: #game has not been won , but game ends as lives exceeded
            print(f"Oh no! You have run out of lives! The correct word was {chosen_word}.")
            print("Better luck next time.")
        #stats
        total_session_games += 1
        session_duration = round(time.time() - game_start, 0) #calculates total session duration 
        print(f"Total games you have played in this session: {total_session_games}")
        print(f"Total wins in this session: {total_wins}")
        print(f"Total session duration: {session_duration} seconds. Make sure you take a break soon!") # convert this into minutes, break if over 5 minutes!!
       
        game_active = get_yes_no_input("Would you like to play again?")


#game trigger
    
if __name__ == "__main__": #executes the game, only if directly running script
    main()
    




