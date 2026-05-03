import pytest
from logic import HangmanGame, SessionStats

# ==========================================
# 8 TESTS FOR HangmanGame
# ==========================================

def test_correct_guess_updates_state():
    """Happy Path: A correct guess reveals letters and updates counts."""
    game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    is_correct, occurrences = game.evaluate_guess("p")
    
    assert is_correct == True
    assert occurrences == 2
    assert game.correct_guesses == 2
    assert game.lives == 5
    assert "p" in game.guessed_letters
    assert game.display_word == ['_', 'p', 'p', '_', '_']
    assert game.game_won == False
    assert game.start_time > 0
    assert game.total_guesses == 1
    
def test_incorrect_guess_loses_life():
    """Sad Path: An incorrect guess drops a life but keeps correct guesses at 0."""
    game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    is_correct, occurrences = game.evaluate_guess("z")
    
    assert is_correct == False
    assert occurrences == 0
    assert game.lives == 4
    assert game.correct_guesses == 0
    assert "z" in game.guessed_letters
    assert game.display_word == ['_', '_', '_', '_', '_']
    assert game.game_won == False
    assert game.start_time > 0
    assert game.total_guesses == 1

def test_winning_condition_triggered():
    """Tests that the game sets game_won to True when all letters are guessed."""
    game = HangmanGame(chosen_word="cat", starting_lives=5)
    
    game.evaluate_guess("c")
    game.evaluate_guess("a")
    game.evaluate_guess("z")
    game.evaluate_guess("t")
    
    assert game.game_won == True
    assert game.total_guesses == 4
    
@pytest.mark.parametrize("bad_guess, expected_error", [
    ("ab", "You must enter exactly one character."),     
    ("1", "Your guess must be a letter, no numbers or symbols."), 
    ("!", "Your guess must be a letter, no numbers or symbols.")  
])
def test_invalid_guesses_are_caught(bad_guess, expected_error):
    """Edge Cases: Tests various invalid inputs."""
    game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    is_valid, error_msg = game.is_valid_guess(bad_guess)
    
    assert is_valid == False
    assert error_msg == expected_error
    
def test_duplicate_guess_is_caught():
    """Edge Case: Tests that guessing the same letter twice returns an error."""
    game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    game.evaluate_guess("a") 
    
    is_valid, error_msg = game.is_valid_guess("a")
    
    assert is_valid == False
    assert error_msg == "You have already guessed this letter!"

# ==========================================
# TESTS FOR SessionStats
# ==========================================

def test_session_stats_records_wins_correctly():
    stats = SessionStats()
    
    stats.record_game(game_won=True, time_elapsed=45.0)
    stats.record_game(game_won=False)
    
    assert stats.total_games == 2
    assert stats.total_wins == 1
    assert stats.winning_times == [45.0]
    assert stats.get_win_percentage() == 50.0

