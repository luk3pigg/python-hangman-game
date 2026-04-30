import time

class HangmanGame:
    def __init__(self, chosen_word, starting_lives):
        # Baseline stats
        self.chosen_word = chosen_word
        self.lives = starting_lives
        #State tracking
        self.display_word = ['_'] * len(self.chosen_word)
        self.correct_guesses = 0
        self.guessed_letters = []
        self.total_guesses = 0
        self.game_won = False
        self.start_time = time.time()
    def evaluate_guess(self, letter_guess):
        """
        Processes a valid letter guess, updates the game state, 
        checks for win/loss conditions, and returns a tuple for UI feedback: (is_correct_boolean, occurrences)
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
            #receipt for a correct guess
            return True, occurrences
        else:
            self.lives -= 1
            return False, 0
    def is_valid_guess(self, guess):
        """
        Validates the guess and returns a tuple: (is_valid_boolean, error_message)
        """
        if len(guess) != 1: 
            return False, "You must enter exactly one character."
        if not guess.isalpha():
            return False, "Your guess must be a letter, no numbers or symbols."
    
        if guess in self.guessed_letters:
            return False, "You have already guessed this letter!"
        return True, ""

class SessionStats:
    def __init__(self):
        self.total_games = 0
        self.total_wins = 0
        self.winning_times = []
        self.session_start_time = time.time()
    def record_game(self, game_won, time_elapsed=None): #set default values
        self.total_games += 1    
        if game_won:
            self.winning_times.append(time_elapsed)
            self.total_wins += 1
    def get_win_percentage(self):
        win_percentage = round((self.total_wins / self.total_games) * 100, 1)
        return win_percentage
    def get_session_duration(self):
        session_duration_total_seconds = int(time.time() - self.session_start_time) 
        minutes = session_duration_total_seconds // 60
        seconds = session_duration_total_seconds % 60
        return minutes, seconds
        
        
    


