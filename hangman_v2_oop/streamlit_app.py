import streamlit as st
import json
import random
import time
from logic import HangmanGame, SessionStats

# ==========================================
# 1. SESSION STATE SETUP
# ==========================================
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'game' not in st.session_state:
    st.session_state.game = None
if 'session_stats' not in st.session_state:
    st.session_state.session_stats = SessionStats()
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'guess_error' not in st.session_state:
    st.session_state.guess_error = None

# ==========================================
# 2. HELPER FUNCTIONS & CALLBACKS
# ==========================================
def navigate(page_name):
    """Changes the current page in memory."""
    st.session_state.page = page_name
    st.session_state.guess_error = None # Clear errors on page change

def get_random_word(target_length):
    """Loads a word from the JSON file based on the slider length."""
    try:
        with open("word_bank.json", "r") as file:
            word_bank = json.load(file)
            # Filter words by the requested length
            return random.choice(word_bank[str(target_length)])
    except FileNotFoundError:
        return "python" # Fallback if file is missing

def start_new_game(lives, length):
    """Initializes the engine and switches to the game screen."""
    word = get_random_word(length)
    st.session_state.game = HangmanGame(chosen_word=word, starting_lives=lives)
    st.session_state.start_time = time.time()
    st.session_state.starting_lives = lives 
    st.session_state.guess_error = None
    navigate('game')

def process_guess():
    """This runs EXACTLY when the user hits Enter, BEFORE the screen redraws."""
    guess = st.session_state.guess_input.lower()
    st.session_state.guess_input = "" # Immediately clear the text box
    
    if guess:
        game = st.session_state.game
        is_valid, error_msg = game.is_valid_guess(guess)
        
        if not is_valid:
            st.session_state.guess_error = error_msg
        else:
            st.session_state.guess_error = None
            game.evaluate_guess(guess)
            
            # Check Win/Loss conditions immediately
            if game.game_won or game.lives <= 0:
                time_elapsed = round(time.time() - st.session_state.start_time, 1)
                st.session_state.session_stats.record_game(game.game_won, time_elapsed)
                st.session_state.time_elapsed = time_elapsed
                navigate('post_game')


# ==========================================
# 3. SCREEN RENDERERS
# ==========================================

# --- SCREEN: WELCOME ---
if st.session_state.page == 'welcome':
    st.title("Hangman Web Pro Beta Version🌐")
    st.write("Welcome to the ultimate Hangman experience.")
    
    col1, col2 = st.columns(2)
    with col1:
        chosen_lives = st.slider("Starting Lives", min_value=5, max_value=10, value=5)
    with col2:
        chosen_length = st.slider("Word Length", min_value=5, max_value=10, value=5)
        
    st.button("Start Game", type="primary", on_click=start_new_game, args=(chosen_lives, chosen_length))
    st.button("How to Play", on_click=navigate, args=('rules',))

# --- SCREEN: RULES ---
elif st.session_state.page == 'rules':
    st.title("How to Play")
    st.markdown("""
    1. Choose your word length and lives.
    2. Guess letters one by one.
    3. If you guess wrong, you lose a life.
    4. Guess the whole word before lives run out!
    """)
    st.button("Back to Menu", on_click=navigate, args=('welcome',))

# --- SCREEN: THE GAME ---
elif st.session_state.page == 'game':
    game = st.session_state.game
    
    st.title("Hangman")
    
    # 1. Display the Word
    st.header(" ".join(game.display_word))
    st.markdown("---")
    
    # 2. Display the Stats & Guessed Letters
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"❤️ **Lives Remaining:** {game.lives}")
    with col2:
        # Sort the guessed letters alphabetically for a clean look
        guessed_list = sorted(list(game.guessed_letters))
        guessed_string = ", ".join(guessed_list) if guessed_list else "None"
        st.write(f"📝 **Guessed Letters:** {guessed_string}")
        
    st.markdown("---")
    
    # 3. Show validation errors (like typing a number or duplicate letter)
    if st.session_state.guess_error:
        st.error(st.session_state.guess_error)
        
    # 4. The Input Box (Notice the 'on_change' parameter!)
    st.text_input("Enter a letter and press Enter:", 
                  max_chars=1, 
                  key="guess_input", 
                  on_change=process_guess) # forces input here to be max 1 letter anyway!

# --- SCREEN: POST-GAME ---
elif st.session_state.page == 'post_game':
    game = st.session_state.game
    stats = st.session_state.session_stats
    
    if game.game_won:
        st.balloons()
        st.success("🎉 You Won! 🎉")
    else:
        st.error(f"💀 Game Over! The word was: **{game.chosen_word}**")
        
    st.subheader("Game Stats")
    total_guesses = game.correct_guesses + (st.session_state.starting_lives - game.lives)
    st.write(f"⏱️ **Time:** {st.session_state.time_elapsed} seconds")
    st.write(f"🎯 **Total Guesses:** {total_guesses}")
    
    st.subheader("Session Stats")
    st.write(f"🎮 **Total Games:** {stats.total_games}")
    st.write(f"🏆 **Win Rate:** {stats.get_win_percentage()}%")
    
    st.button("Play Again", type="primary", on_click=navigate, args=('welcome',))