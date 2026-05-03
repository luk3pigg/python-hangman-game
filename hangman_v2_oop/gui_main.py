import tkinter as tk
import json
import random
import time
from logic import HangmanGame, SessionStats

# ==========================================
# 1. CORE SETUP & STATE
# ==========================================
root = tk.Tk()
root.title("Hangman Desktop Pro")
root.geometry("450x550")

# Global State Variables
session_stats = SessionStats()
game = None
start_time = 0

# Create all our invisible containers (Frames)
welcome_frame = tk.Frame(root)
rules_frame = tk.Frame(root)
game_frame = tk.Frame(root)
post_game_frame = tk.Frame(root)

def show_frame(frame_to_show):
    """Hides all frames, then displays the requested one."""
    for frame in (welcome_frame, rules_frame, game_frame, post_game_frame):
        frame.pack_forget()
    frame_to_show.pack(fill="both", expand=True, pady=20)

def get_random_word(target_length):
    """Loads a word from the JSON file based on the slider length."""
    try:
        with open("data/word_bank.json", "r") as file:
            word_bank = json.load(file)
            # Filter words by the requested length
            return random.choice(word_bank[str(target_length)])
    except FileNotFoundError:
        return "python" # Fallback if file is missing

# ==========================================
# 2. SCREEN: RULES
# ==========================================
tk.Label(rules_frame, text="How to Play", font=("Helvetica", 20, "bold")).pack(pady=10)
rules_text = (
    "OBJECTIVE: guess the secret word by guessing the letters it contains!\n"
    "1.) Choose how many lives you have.\n" 
    "2.) Choose the length of the secret word.\n"
    "3.) Start guessing letters!"
    "If your letter guess is in the secret word, its location/s in the secret word will be revealed!\n"
    "But be careful: if your letter guess is not in the secret word, you will lose a life.\n"
    "You win the game if you guess all the letters and hence the word without losing all your lives!"
)
tk.Label(rules_frame, text=rules_text, font=("Helvetica", 12), justify="left").pack(pady=20)
tk.Button(rules_frame, text="Back to Menu", command=lambda: show_frame(welcome_frame)).pack()

# ==========================================
# 3. SCREEN: POST-GAME STATS
# ==========================================
pg_title = tk.Label(post_game_frame, text="Game Over", font=("Helvetica", 24, "bold"))
pg_title.pack(pady=10)

pg_game_stats = tk.Label(post_game_frame, text="", font=("Helvetica", 12))
pg_game_stats.pack(pady=10)

pg_session_stats = tk.Label(post_game_frame, text="", font=("Helvetica", 12))
pg_session_stats.pack(pady=10)

tk.Button(post_game_frame, text="Play Again", bg="green", fg="white", font=("Helvetica", 14), 
          command=lambda: show_frame(welcome_frame)).pack(pady=10)
tk.Button(post_game_frame, text="Exit Game", bg="red", fg="white", font=("Helvetica", 14), 
          command=root.destroy).pack()

def trigger_end_game():
    """Calculates stats, updates labels, and shows the post-game screen."""
    time_elapsed = round(time.time() - start_time, 1)
    
    # Record stats in our logic engine
    session_stats.record_game(game.game_won, time_elapsed)
    
    # Update UI Labels
    if game.game_won:
        pg_title.config(text="You Won! 🎉", fg="green")
    else:
        pg_title.config(text=f"You Lost! Word: {game.chosen_word}", fg="red")
        
    pg_game_stats.config(text=f"Time: {time_elapsed}s | Guesses: {game.correct_guesses + (lives_var.get() - game.lives)}")
    
    # Session Stats
    minutes, seconds = session_stats.get_session_duration()
    stats_text = (
        f"--- Session Stats ---\n"
        f"Total Games: {session_stats.total_games}\n"
        f"Win Rate: {session_stats.get_win_percentage()}%\n"
        f"Total session duration: {minutes} minutes, {seconds} seconds."
    )
    pg_session_stats.config(text=stats_text)
    
    show_frame(post_game_frame)

# ==========================================
# 4. SCREEN: THE GAME ENGINE
# ==========================================
word_label = tk.Label(game_frame, text="", font=("Helvetica", 24, "bold"))
word_label.pack(pady=20)

lives_label = tk.Label(game_frame, text="", font=("Helvetica", 14))
lives_label.pack()

status_label = tk.Label(game_frame, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

guess_entry = tk.Entry(game_frame, font=("Helvetica", 18), width=5, justify="center")
guess_entry.pack(pady=10)

def make_guess(event=None):
    """The event=None allows this to be triggered by a Button click OR the Enter key."""
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    is_valid, error_msg = game.is_valid_guess(guess)
    if not is_valid:
        status_label.config(text=error_msg, fg="red")
        return
        
    game.evaluate_guess(guess)
    word_label.config(text=" ".join(game.display_word))
    lives_label.config(text=f"Lives: {game.lives}")
    
    if game.game_won or game.lives <= 0:
        trigger_end_game()
    else:
        status_label.config(text="Good guess!" if guess in game.chosen_word else "Wrong guess!", fg="black")

# Bind the Enter key to the entry box
guess_entry.bind("<Return>", make_guess)

tk.Button(game_frame, text="Guess", command=make_guess, font=("Helvetica", 14)).pack()

# ==========================================
# 5. SCREEN: MAIN MENU (Welcome)
# ==========================================
tk.Label(welcome_frame, text="Welcome to Hangman!", font=("Helvetica", 20, "bold")).pack(pady=10)

tk.Button(welcome_frame, text="How to Play", command=lambda: show_frame(rules_frame)).pack(pady=5)

# Variables to track sliders
lives_var = tk.IntVar(value=6)
length_var = tk.IntVar(value=6)

tk.Label(welcome_frame, text="Starting Lives:").pack(pady=(20,0))
tk.Scale(welcome_frame, from_=5, to=10, orient="horizontal", variable=lives_var).pack()

tk.Label(welcome_frame, text="Word Length:").pack(pady=(10,0))
tk.Scale(welcome_frame, from_=5, to=10, orient="horizontal", variable=length_var).pack()

def start_game():
    global game, start_time
    start_time = time.time()
    
    chosen_lives = lives_var.get()
    chosen_length = length_var.get()
    chosen_word = get_random_word(chosen_length)
    
    game = HangmanGame(chosen_word=chosen_word, starting_lives=chosen_lives)
    
    # Reset Game UI
    word_label.config(text=" ".join(game.display_word))
    lives_label.config(text=f"Lives: {game.lives}")
    status_label.config(text="Type a letter and guess!", fg="black")
    
    show_frame(game_frame)

tk.Button(welcome_frame, text="Start Game", font=("Helvetica", 16), bg="green", fg="white", command=start_game).pack(pady=30)

# ==========================================
# 6. IGNITION
# ==========================================
show_frame(welcome_frame) # Ensure the menu is the first thing we see
root.mainloop()