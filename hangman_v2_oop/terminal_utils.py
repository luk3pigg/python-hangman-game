import os
import time
import random
import statistics


#general UI helper functions


def clear_screen():
    # Clears the terminal screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_yes_no_input(prompt):
    """
    Handles the UI loop for asking the user a generic yes/no question.
    Returns True for 'y', False for 'n'.
    """
    prompt = f"{prompt}\n(y/n) \n> "
    
    while True:
        # The Single Safety Zone
        response = input(prompt).lower().strip()
        
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            # Update the prompt for the next loop
            prompt = "\n[!] Unfortunately, that's an invalid input. Please try again.\n(y/n) \n> "

def input_within_range(lower, upper, prompt, subject):
    while True:
        try:
            user_input = int(input(prompt))
            if lower <= user_input <= upper:
                return user_input 
            else:
                prompt = (f"\n[!] That is not within the specified range for the {subject}. Please enter a number between {lower} and {upper} inclusive.\n> ")
        except ValueError:
            prompt = (f"\n[!] That is not a valid number. Please enter a valid {subject} between {lower} and {upper} inclusive.\n> ")


#game setup helper functions


def load_game(prompt):
    game_active = get_yes_no_input(prompt)
    if not game_active: 
        time.sleep(0.3)
        print("\nGot it. Have a nice day!")
        time.sleep(0.3)
        return #guard clause
    return game_active

def print_rules_if_needed(first_cycle):
    clear_screen()
    time.sleep(0.3)
    if first_cycle: #this function only runs for first cycle
        if get_yes_no_input("\nWould you like to know the rules before we begin?"):
            time.sleep(0.3)
            print("\nThese are the rules:\n\nOBJECTIVE: guess the secret word by guessing the letters it contains!\n>You will choose how many lives you have, and the length of the secret word.\n>If your letter guess is in the secret word, its location/s in the secret word will be revealed!\n>But be careful: if your letter guess is not in the secret word, you will lose a life.\n>You win the game if you guess all the letters and hence the word without losing all your lives!")
            time.sleep(0.3)
            print("\nSo, without further ado...")
        else:
            time.sleep(0.3)
            print("\nOkay, if you say so... ;)")
    return False # Returns False so first_cycle is deactivated forever. # indented exactly here: first time game loads, it sees this, and set to False forver after. This is never seen again 

def setup_game_parameters(word_bank):
    time.sleep(0.3)
    word_length = input_within_range(5, 10, "\nPlease select how many letters you would like the secret word to have, between 5 and 10.\n> ", "word length") 
    chosen_word = random.choice(word_bank[str(word_length)])
    
    time.sleep(0.3)
    lives = input_within_range(5, 10, "\nPlease select how many lives you would like, between 5 and 10.\n> ", "number of lives")
    return chosen_word, lives


#game phase helper functions


def print_turn_status(game):
    """Handles all terminal UI updates for the start of a turn."""
    if game.total_guesses == 0: #these messages only shwo up for the very first go
        print("\nThe timer is on!")
        time.sleep(0.5)
        print("\nThis is your first guess!")
        print(f"\nYou currently have {game.lives} lives.")
        print("\nThis is the secret word:\n")
        print(*game.display_word)
    else:
        elapsed_time = int(time.time() - game.start_time)
        print(f"\n{elapsed_time} seconds have gone so far!") 
        print(f"\nThis is guess number {game.total_guesses + 1}.")
        if game.lives == 1:
            print("\n[!] Careful! You have 1 life remaining.")
        else:
            print(f"\nYou currently have {game.lives} lives.")
        if game.correct_guesses == 1:
            print("\nYou currently have 1 correct guess.")
        else:    
            print(f"\nYou currently have {game.correct_guesses} correct guesses.")
        print("\nYou have guessed the following letters:\n")
        print(*game.guessed_letters)
        print("\nHere's what you know so far:\n")
        print(*game.display_word)            
   
def get_letter_guess(game):
    """Prompts the user for a valid, single letter that hasn't been guessed yet."""
    prompt = "\nPlease enter a letter guess:\n>  "
    while True:
        # 1. The Single Safety Zone
        letter_guess = input(prompt).lower().strip()
        
        # 2. Run the engine ONCE and unpack the tuple into two variables
        is_valid, error_msg = game.is_valid_guess(letter_guess)
        
        # 3. Logic Routing
        if is_valid:
            return letter_guess 
        else:
            prompt = f"\n[!] {error_msg} Please try another guess:\n> "
            
def play_single_game(game):
    """Runs the while loop for a single game and returns the time elapsed."""
    clear_screen()
    time.sleep(0.3)
    
    while game.lives > 0 and not game.game_won:
        print_turn_status(game)
        letter_guess = get_letter_guess(game)
        is_correct, occurrences = game.evaluate_guess(letter_guess)
        
        clear_screen()
        if is_correct:
            print("Correct guess!")
            time.sleep(1.0)
            if occurrences == 1: print("\nYour guess appears in the secret word once.")
            else: print(f"\nYour guess appears in the secret word {occurrences} times!")
            time.sleep(1.0)
        else:
            print("Incorrect guess...Unlucky!") 
            time.sleep(1.0)
            
    # Calculate and return time elapsed when loop breaks - calculates now rather than waiting for next bit which includes a time.sleep()
    return round(time.time() - game.start_time, 0)


#post game helper functions


def print_post_game_stats(game, stats, time_elapsed):
    clear_screen()
    time.sleep(0.3)
    
    # 1. Individual Game Outcomes
    if game.game_won:
        stats.record_game(game_won=True, time_elapsed=time_elapsed)
        average_time = round(statistics.mean(stats.winning_times), 0)
        print(f"You won! The secret word was {game.chosen_word}!\n")
        time.sleep(1.0)
        print("----------GAME STATISTICS----------\n")
        print(f"You took {time_elapsed} seconds.\n")
        if time_elapsed == min(stats.winning_times) and len(stats.winning_times) > 1:
            time.sleep(1.0)
            print("WOW! That's your fastest winning time yet!\n")
        time.sleep(1.0)
        print(f"Your average winning time is {average_time} seconds!\n")
    else:
        stats.record_game(game_won=False)
        print(f"Oh no! You have run out of lives! The correct word was {game.chosen_word}.\n")
        time.sleep(1.0)
        print("Better luck next time.\n")
        
    # 2. Session Outcomes
    minutes, seconds = stats.get_session_duration()
    print("----------SESSION STATISTICS----------")
    print(f"\nTotal games you have played in this session: {stats.total_games}")
    print(f"Total wins in this session: {stats.total_wins} ({stats.get_win_percentage()} % win rate)")
    print(f"Total session duration: {minutes} minutes, {seconds} seconds.") 
    
    time.sleep(1.0)
    if minutes >= 5: print("\nYou have been playing for over 5 minutes. Make sure you take a break soon!")
    time.sleep(1.0)