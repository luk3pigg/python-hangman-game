from logic import HangmanGame, SessionStats
import utils_ui as ui
import json
import sys

#define load word bank in main rather than putting in UI utils file
def load_word_bank(filepath):
    """Attempts to load the word bank JSON file."""
    try:
        with open(filepath, "r") as file:
            return json.load(file) #data externalisation to avoid hard-coding word bank
    except FileNotFoundError:
        ui.clear_screen()
        print("[!] 'word_bank.json' is missing. Please ensure the file is in the same folder as this script.")
        sys.exit() # This cleanly shuts down the program

#main game engine
def main():     
    #load data
    
    WORD_BANK = load_word_bank("word_bank.json")
    
    #init stats
    stats = SessionStats()
    
    #greeting
    
    game_active = ui.load_game("\nWelcome! Are you ready to play hangman?")
    
    first_cycle = True #first cycle is different - asks for rules etc 
    
    #Main session loop
    
    while game_active:   
        
        #1 Print rules if required
        
        first_cycle = ui.print_rules_if_needed(first_cycle) #always set to False from here on 
        
        #2 Setup game parameters and instantiate object
        #eventually change word length lower upper to min/max of imported list - might uses pandas, wait for this first.
        chosen_word, lives = ui.setup_game_parameters(WORD_BANK)
        
        #3 Instantiate game object
        
        game = HangmanGame(chosen_word, lives)
        
        #4 Play the game
        
        time_elapsed = ui.play_single_game(game)
        
        #5 Evaluate Outcomes
        
        ui.print_post_game_stats(game, stats, time_elapsed)
        
        #6 Play Again?
        game_active = ui.load_game("\nWould you like to play again?")
        
#game trigger

if __name__ == "__main__": 
    try:
        ui.clear_screen()
        main()
    except KeyboardInterrupt:
        # This catches the Ctrl+C abort command!
        ui.clear_screen()
        print("\nGame aborted by user. Goodbye!\n")
        sys.exit()
    




