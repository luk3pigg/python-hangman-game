import game_functions as gf
import time
import statistics
import json
import sys
import os

try:
    with open("word_bank.json", "r") as file:
        WORD_BANK = json.load(file) #data externalisation to avoid hard-coding word bank
except FileNotFoundError:
    print("[!] 'word_bank.json' is missing. Please ensure the file is in the same folder as this script.")
    sys.exit() # This cleanly shuts down the program

#UI helper functions

def clear_screen():
    # Clears the terminal screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print 50 blank lines as a fallback to push old text out of view
    # (Real terminals will just clear, IDEs will print the spaces)
    #print("\n" * 50)

def get_yes_no_input(prompt):
    """
    Handles the UI loop for asking the user a generic yes/no question.
    Inputs the generic question, Returns True for 'y', False for 'n'.
    
    """
    response = input(f"{prompt}\n(y/n) \n> ").lower().strip()
    while True:
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            response = input("\n[!] Unfortunately, that's an invalid input. Please try again.\n(y/n) \n> ")
 
def input_within_range(lower, upper, prompt, subject):
    while True:
        try:
            user_input = int(input(prompt))
            if lower <= user_input <= upper:
                return user_input 
            else:
                prompt = (f"\nThat is not within the specified range for the {subject}. Please enter a number between {lower} and {upper} inclusive.\n> ")
        except ValueError:
            prompt = (f"\nThat is not a valid number. Please enter a valid {subject} between {lower} and {upper} inclusive.\n> ")

def print_turn_status(total_guesses, lives, display_word, correct_guesses, guessed_letters, start_time):
    """Handles all terminal UI updates for the start of a turn."""
    if total_guesses == 0: #these messages only shwo up for the very first go
        print("\nThe timer is on!")
        print("\nThis is your first guess!")
        print(f"\nYou currently have {lives} lives.")
        print("\nThis is the secret word:")
        print(*display_word)
    else:
        elapsed_time = int(time.time() - start_time)
        print(f"\n{elapsed_time} seconds have gone so far!") 
        print(f"\nThis is guess number {total_guesses + 1}.")
        print(f"\nYou currently have {lives} lives.")
        print(f"\nYou currently have {correct_guesses} correct guesses.")
        print("\nYou have guessed the following letters:")
        print(*guessed_letters)
        print("\nHere's what you know so far:")
        print(*display_word)            
   
def get_letter_guess(guessed_letters):
    """Prompts the user for a valid, single letter that hasn't been guessed yet."""
    while True:
        letter_guess = input("\n\n\nPlease enter a letter guess: ").lower().strip()
    
        # We still rely on the engine for the logic!
        if gf.is_valid_guess(letter_guess, guessed_letters): 
            return letter_guess 
        else:
            print("\n\n\nThat guess was invalid. Ensure the guess is a single letter that hasn't already been guessed!")
         
#main game engine
def main(): #master function protects global variables by transforming into local variables
    #clear_screen()    
#global 'overall session' stats
    total_session_games = 0 
    total_wins = 0
    winning_times = []
    
    
                   
    game_active = get_yes_no_input("\nWelcome! Are you ready to play hangman?") #Initialisation of game
    #clear_screen()
    if not game_active: #if game_active is False because user entered 'n'...
        print("\nGot it. Have a nice day!") #exits the game here
        return #guard clause: prevents the next 2 lines from ever being run (unneccesary background work). However without this 'return', code would still work due to while game_active loop
    game_start = time.time() #overall timer starts
    first_cycle = True #first cycle is different - asks for rules etc 
    while game_active:   #loop for each session
        clear_screen()
        if first_cycle: #this inner loop only runs for the first cycle
            wants_rules = get_yes_no_input("\nWould you like to know the rules before we begin?")
            
            if wants_rules:
                #clear_screen()
                print("\nThese are the rules:\nOBJECTIVE: guess the secret word by guessing the letters it contains!\nYou will choose how many lives you have, and the length of the secret word.\nIf your letter guess is in the secret word, its location/s in the secret word will be revealed!\nBut be careful: if your letter guess is not in the secret word, you will lose a life.\nYou win the game if you guess all the letters and hence the word without losing all your lives!\n\nSo, without further ado....")
            else:
                #clear_screen()
                print("\nCool.")
            first_cycle = False # indented exactly here: first time game loads, it sees this, and set to False forver after. This is never seen again 
                
        word_length_lower = 5 #eventually change these to min/max of imported list - might uses pandas, wait for this first. 
        word_length_upper = 10
        word_length_input = input_within_range(lower=word_length_lower, upper=word_length_upper, prompt=f"\nPlease select how many letters you would like the secret word to have, between {word_length_lower} and {word_length_upper}.\n> ", subject="word length") 
        
        chosen_word = gf.select_word(word_list = WORD_BANK[str(word_length_input)]) #accesses dictionary with key=word length and uses function in other file
        
        lives_lower = 5
        lives_upper = 10
        lives = input_within_range(lower=lives_lower, upper=lives_upper, prompt=f"\nPlease select how many lives you would like, between {lives_lower} and {lives_upper}.\n> ", subject="number of lives")
        
        #Initialisation of each individual game
        
        #game state (individual agme stats) variables
        correct_guesses = 0
        guessed_letters = []
        display_word = ['_'] * len(chosen_word)
        total_guesses = 0
        game_won = False
        start_time = time.time() #starts time for individual game
    
        
    
    
        #clear_screen()
        while lives > 0 and not game_won: #loop for each individual game. For this loop to run, both have to be true: lives >0 AND game has not been won ie correct guesses = length of word 
            # 1. Update the UI
            print_turn_status(
                total_guesses=total_guesses, 
                lives=lives, 
                display_word=display_word, 
                correct_guesses=correct_guesses, 
                guessed_letters=guessed_letters, 
                start_time=start_time
            )
            
        # 2. Ask the user for their letter guess
            
            letter_guess = get_letter_guess(guessed_letters)
            #clear_screen()
        
        # 3. Update turn counter
        
            total_guesses += 1
                    
        # 4. Pass the guess into gf.guess_result() to update the state   
            
            lives, correct_guesses, game_won = gf.guess_result(guessed_letters, chosen_word, display_word, letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses, game_won=game_won) #updates whether the game has been won yet or not, and whether all lives have been used up yet or not - these 2 factors decide if the game has ended or not. 
            if letter_guess in chosen_word:
                occurrences = chosen_word.count(letter_guess)
                print("\n\n\nCorrect guess!")
                time.sleep(1.0)
                print(f"Your guess appears in the secret word {occurrences} times!")
                time.sleep(1.0)
            else:
                print("\n\n\nIncorrect guess...Unlucky!") #these print statements remain in UI, all logic goes into game_functions.py 
        
        #end game  
        
        if game_won: #only runs when correct guesses = number of letters in the word 
            end_time = time.time() #ends the individual game time 
            time_elapsed = round(end_time - start_time, 2) #calculates total individual game time
            winning_times.append(time_elapsed)
            average_time = round(statistics.mean(winning_times), 2)
            total_wins += 1
            print(f"\n\nYou won! The secret word was {chosen_word}!")
            print(f"You took {time_elapsed} seconds.")
            if time_elapsed == min(winning_times) and len(winning_times) > 1:
                print("WOW! That's your fastest winning time yet!")
            print(f"Your average winning time is {average_time} seconds!")
            #win percentage
            #average time taken for the wins
        else: #game has not been won , but game ends as lives exceeded
            print(f"Oh no! You have run out of lives! The correct word was {chosen_word}.")
            print("Better luck next time.")
        #session stats
        # --- SESSION STATS ---
        total_session_games += 1
        
        # 1. Calculate Win Percentage
        win_percentage = round((total_wins / total_session_games) * 100, 1)
        
        # 2. Calculate Minutes and Seconds
        session_duration_total_seconds = int(time.time() - game_start) 
        minutes = session_duration_total_seconds // 60
        seconds = session_duration_total_seconds % 60
        
        print(f"\nTotal games you have played in this session: {total_session_games}")
        print(f"Total wins in this session: {total_wins} ({win_percentage} % win rate)")
        print(f"Total session duration: {minutes} minutes, {seconds} seconds.") 
        
        # 3. The 5-Minute Break Warning
        if minutes >= 5:
            print("You have been playing for over 5 minutes. Make sure you take a break soon!")
       
        game_active = get_yes_no_input("Would you like to play again?")
        if not game_active: #if game_active is False because user entered 'n'...
            print("\nGot it. Have a nice day!") #exits the game here


#game trigger
#clear_screen() 
if __name__ == "__main__": #executes the game, only if directly running script
    main()
    




