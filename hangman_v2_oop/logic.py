import time

class HangmanGame:
    """
    Manages the state and core logic for a single game of Hangman.
    """
    def __init__(self, chosen_word, starting_lives):
        """
        Initialises a new Hangman game instance.

        Args:
            chosen_word (str): The secret word to be guessed.
            starting_lives (int): The number of incorrect guesses allowed.
        """
        # Baseline stats
        self.chosen_word = chosen_word
        self.lives = starting_lives
        #Game State tracking
        self.display_word = ['_'] * len(self.chosen_word)
        self.correct_guesses = 0
        self.guessed_letters = []
        self.total_guesses = 0
        self.game_won = False
        self.start_time = time.time()
    
    def evaluate_guess(self, letter_guess):
        """
        Processes a valid letter guess, updates the internal game state, 
        and checks for win/loss conditions.

        Args:
            letter_guess (str): The validated, lowercase letter guessed by the user.

        Returns:
            tuple[bool, int]: A tuple containing a boolean indicating if the guess 
                              was correct, and an integer representing the number 
                              of times the letter occurred in the word.
        """
        self.guessed_letters.append(letter_guess)
        self.total_guesses += 1
        
        if letter_guess in self.chosen_word:
            occurrences = 0
            for i, letter in enumerate(self.chosen_word):
                if letter == letter_guess:
                    occurrences += 1
                    self.display_word[i] = letter_guess
            
            self.correct_guesses += occurrences
            
            if self.correct_guesses == len(self.chosen_word):
                self.game_won = True
            
            return True, occurrences
        else:
            self.lives -= 1
            return False, 0
    
    def is_valid_guess(self, guess):
        """
        Validates the user's raw string input against game rules.

        Args:
            guess (str): The raw string input provided by the user.

        Returns:
            tuple[bool, str]: A tuple containing a boolean indicating if the guess 
                              is valid, and a string containing an error message if invalid.
        """
        if len(guess) != 1: 
            return False, "You must enter exactly one character."
        if not guess.isalpha():
            return False, "Your guess must be a letter, no numbers or symbols."
    
        if guess in self.guessed_letters:
            return False, "You have already guessed this letter!"
        return True, ""

class SessionStats:
    """
    Tracks aggregate statistics and time elapsed across multiple Hangman games.
    """
    def __init__(self):
        """Initialises a new session with zeroed baseline stats."""
        self.total_games = 0
        self.total_wins = 0
        self.winning_times = []
        self.session_start_time = time.time()
    
    def record_game(self, game_won, time_elapsed=None):
        """
        Logs the results of a completed game into the session tracker.

        Args:
            game_won (bool): True if the player won the game, False otherwise.
            time_elapsed (float, optional): Total seconds the game took to complete. 
                                            Defaults to None.
        """
        self.total_games += 1    
        if game_won:
            self.winning_times.append(time_elapsed)
            self.total_wins += 1
    
    def get_win_percentage(self):
        """
        Calculates the player's win rate for the current session.

        Returns:
            float: The win percentage rounded to one decimal place. Returns 0.0 
                   if no games have been played to prevent division by zero.
        """
        if self.total_games == 0:
            return 0.0 #ensures true independence of object by protecting against ZeroDivisionError even though main will never get to this stage!
        win_percentage = round((self.total_wins / self.total_games) * 100, 1)
        return win_percentage
    
    def get_session_duration(self):
        """
        Calculates the total time elapsed since the session was initialised.

        Returns:
            tuple[int, int]: A tuple representing the elapsed time in (minutes, seconds).
        """
        session_duration_total_seconds = int(time.time() - self.session_start_time) 
        minutes = session_duration_total_seconds // 60
        seconds = session_duration_total_seconds % 60
        return minutes, seconds
        
        
    


