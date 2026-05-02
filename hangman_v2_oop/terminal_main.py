from logic import HangmanGame, SessionStats
import terminal_utils as ui
import json
import sys

def load_word_bank(filepath):
    """
    Attempts to load the word bank JSON file into memory.
    
    Args:
        filepath (str): The relative path to the JSON data file.
        
    Returns:
        dict: The parsed JSON data containing word lengths and word lists.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        ui.clear_screen()
        print(f"[!] CRITICAL ERROR: '{filepath}' is missing. Please ensure the file is in the same folder as this script.")
        sys.exit(1) 

def main():     
    """
    The main orchestrator for the terminal Hangman experience.
    Delegates all complex UI logic and game maths to specialised modules.
    """
    # --- 1. Initialisation ---
    filepath = "data/word_bank.json"
    WORD_BANK = load_word_bank(filepath=filepath)
    
    stats = SessionStats()
    
    game_active = ui.load_game(prompt="\nWelcome! Are you ready to play hangman?")
    first_cycle = True  
    
    # --- 2. The Session Loop ---
    while game_active:   
        
        #1 Game Setup
        
        first_cycle = ui.print_rules_if_needed(first_cycle=first_cycle) #rules only offered for first game
        chosen_word, lives = ui.setup_game_parameters(word_bank=WORD_BANK)
        
        #2 Instantiate Game Object
        
        game = HangmanGame(chosen_word=chosen_word, starting_lives=lives)
        
        #3 Play the game
        
        time_elapsed = ui.play_single_game(game=game)
        
        #4 Evaluate Game Outcomes
        
        ui.print_post_game_stats(game=game, stats=stats, time_elapsed=time_elapsed)
        
        #5 Session Continuation
        game_active = ui.load_game(prompt="\nWould you like to play again?")
        
# ==========================================
# EXECUTION
# ==========================================

if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt:
        ui.clear_screen()
        print("\nGame aborted by user. Goodbye!\n")
        sys.exit(0)
    




