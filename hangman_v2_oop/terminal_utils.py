import os
import time
import random
import statistics

# ==========================================
# 1. GENERAL UI HELPER FUNCTIONS
# ==========================================

def clear_screen():
    """Clears the terminal scrollback depending on the host OS."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_yes_no_input(prompt):
    """
    Prompts the user for a yes/no response and handles invalid inputs.
    
    Args:
        prompt (str): The question to present to the user.
        
    Returns:
        bool: True if user selects 'yes', False if 'no'.
    """
    prompt = f"{prompt}\n(y/n) \n> "
    
    while True:
        response = input(prompt).lower().strip()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            prompt = "\n[!] Unfortunately, that's an invalid input. Please try again.\n(y/n) \n> "

def input_within_range(lower, upper, prompt, subject):
    """
    Forces the user to input a valid integer within a specified range.
    
    Args:
        lower (int): Minimum acceptable value.
        upper (int): Maximum acceptable value.
        prompt (str): The initial prompt text.
        subject (str): Contextual label for error messages (e.g., 'lives').
        
    Returns:
        user_input (int): The validated user input.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if lower <= user_input <= upper:
                return user_input 
            else:
                prompt = (f"\n[!] That is not within the specified range for the {subject}. Please enter a number between {lower} and {upper} inclusive.\n> ")
        except ValueError:
            prompt = (f"\n[!] That is not a valid number. Please enter a valid {subject} between {lower} and {upper} inclusive.\n> ")

# ==========================================
# 2. GAME SETUP HELPER FUNCTIONS
# ==========================================

def load_game(prompt):
   """
    Wraps the yes/no prompt to handle game exit messages.
    
    Args:
        prompt (str): The question to ask the user.
        
    Returns:
        bool: True if the user wants to play, False if they want to exit.
   """
   game_active = get_yes_no_input(prompt)
   if not game_active: 
       time.sleep(0.3)
       print("\nGot it. Have a nice day!")
       time.sleep(0.3)
       return
   return game_active
   

def print_rules_if_needed(first_cycle):
    """
    Prints the game rules if it is the user's first game of the session.
    
    Args:
        first_cycle (bool): A flag indicating if this is the first loop iteration.
        
    Returns:
        bool: Always returns False so the rules are never printed again in this session.
    """
    clear_screen()
    time.sleep(0.3)
    
    if first_cycle: 
        if get_yes_no_input(prompt="\nWould you like to know the rules before we begin?"):
            time.sleep(0.3)
            print("\nThese are the rules:\n\nOBJECTIVE: guess the secret word by guessing the letters it contains!\n>You will choose how many lives you have, and the length of the secret word.\n>If your letter guess is in the secret word, its location/s in the secret word will be revealed!\n>But be careful: if your letter guess is not in the secret word, you will lose a life.\n>You win the game if you guess all the letters and hence the word without losing all your lives!")
            time.sleep(0.3)
            print("\nSo, without further ado...")
        else:
            time.sleep(0.3)
            print("\nOkay, if you say so... ;)")
    return False 

def setup_game_parameters(word_bank):
    """
    Prompts the user for word length and lives, then selects the word.
    
    Args:
        word_bank (dict): The dictionary containing available words mapped by length.
        
    Returns:
        tuple[str, int]: A tuple containing the randomly chosen word and the selected number of lives.
    """
    time.sleep(0.3)
    word_length = input_within_range(lower=5, upper=10, prompt="\nPlease select how many letters you would like the secret word to have, between 5 and 10.\n> ", subject="word length") 
    chosen_word = random.choice(word_bank[str(word_length)])
    
    time.sleep(0.3)
    lives = input_within_range(lower=5, upper=10, prompt="\nPlease select how many lives you would like, between 5 and 10.\n> ", subject="number of lives")
    
    return chosen_word, lives

# ==========================================
# 3. GAME PHASE HELPER FUNCTIONS
# ==========================================

def print_turn_status(game):
    """
    Renders the current game state to the terminal.
    
    Args:
        game (HangmanGame): The current active instance of the Hangman game.
        
    Returns:
        None
    """
    if game.total_guesses == 0:
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
    """
    Prompts the user for a valid, single letter that hasn't been guessed yet.
    
    Args:
        game (HangmanGame): The current active instance of the Hangman game.
        
    Returns:
        str: A validated, lowercase, single-character string.
    """
    prompt = "\nPlease enter a letter guess:\n>  "
    while True:
        letter_guess = input(prompt).lower().strip()
        
        is_valid, error_msg = game.is_valid_guess(guess=letter_guess)
        
        if is_valid:
            return letter_guess 
        else:
            prompt = f"\n[!] {error_msg} Please try another guess:\n> "
            
def play_single_game(game):
    """
    Runs the while loop for a single game and returns the time elapsed.
    
    Args:
        game (HangmanGame): The initialised Hangman game object to be played.
        
    Returns:
        float: The total time elapsed during the game in seconds.
    """
    clear_screen()
    time.sleep(0.3)
    
    while game.lives > 0 and not game.game_won:
        print_turn_status(game=game)
        letter_guess = get_letter_guess(game=game)
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
            
    return round(time.time() - game.start_time, 0)


# ==========================================
# 4. POST GAME HELPER FUNCTIONS
# ==========================================


def print_post_game_stats(game, stats, time_elapsed):
    """
    Evaluates the outcome of a game, updates session stats, and prints results.
    
    Args:
        game (HangmanGame): The completed game instance.
        stats (SessionStats): The object tracking the overall session history.
        time_elapsed (float): Total seconds the individual game took to play.
        
    Returns:
        None
    """
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