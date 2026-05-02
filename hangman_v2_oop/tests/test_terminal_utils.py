import pytest
import utils_ui as ui  # Change this if your file is named utils_ui.py
from logic import HangmanGame

# ==========================================
# TESTS FOR get_yes_no_input
# ==========================================

def test_yes_no_input_accepts_yes(monkeypatch):
    """Happy Path: Tests that typing 'y' immediately returns True."""
    # Hijack the keyboard to instantly type 'y'
    monkeypatch.setattr('builtins.input', lambda prompt: 'y')
    
    result = ui.get_yes_no_input("Are you ready?")
    assert result == True
    
#doesn't matter what prompt we give here - just get the while loop running.
#input y - loop should immediately return True

def test_yes_no_input_recovers_from_invalid(monkeypatch):
    """Sad Path: Tests that typing nonsense is rejected until 'n' is typed."""
    # The robot types 'maybe', then 'idk', and finally gives up and types 'n'
    fake_keyboard = iter(['maybe', 'idk', '!', '47', 'N', 'no', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.get_yes_no_input("Are you ready?")
    assert result == False
    
#iterate through all edge cases - final input is n to ensure loop ends and can return False for correct input of 'n'


# ==========================================
# TESTS FOR input_within_range
# ==========================================

def test_input_within_range_accepts_valid_number(monkeypatch):
    """Happy Path: Tests that typing a correct number works immediately."""
    monkeypatch.setattr('builtins.input', lambda prompt: '7')
    
    result = ui.input_within_range(5, 10, "Pick a number", "test")
    assert result == 7

def test_input_within_range_recovers_from_errors(monkeypatch):
    """
    Sad Path: Tests that the function rejects strings (ValueError) 
    and out-of-bounds numbers before finally accepting a valid input.
    """
    # The robot types a string, then a number too high, then a valid number
    fake_keyboard = iter(['apple', '99', '6'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.input_within_range(5, 10, "Pick a number", "test")
    assert result == 6
    
#don;t need to test for load game, print rules if needed etd - these just getyesno and inputwithinrange, which we have already tested
#also, don't test play_single_game or print_post_game_stats - these are controllers, integration tests, require mocking entire game inputs/loop. Have tested UI and logic.py already so trust these work 


# ==========================================
# TESTS FOR get_letter_guess
# ==========================================

#testing get_letter_guess - can do, but have alredy tested the is_valid_guess logic!


def test_letter_input_returns_letter(monkeypatch):
    """Happy Path: Tests that a valid letter is accepted immediately."""
    
    # 1. Create a dummy game just for this test
    dummy_game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    # 2. Hijack the keyboard to instantly type 'g'
    monkeypatch.setattr('builtins.input', lambda prompt: 'G') #works for both G and g
    
    # 3. Run the function and pass it the dummy game!
    result = ui.get_letter_guess(dummy_game)
    
    # 4. Demand the result is exactly 'g'
    assert result == 'g'
    
def test_letter_input_rejects_bad_guesses(monkeypatch):
    """
    Sad Path: Tests that the function rejects numbers, multiple letters, 
    and already-guessed letters before finally accepting a valid new letter.
    """
    dummy_game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    # Let's force the game to think 'a' has already been guessed
    dummy_game.guessed_letters.append('a')
    
    # The robot types a number, a double letter, an already guessed letter ('a'), 
    # and finally gives a valid letter ('z')
    fake_keyboard = iter(['1', 'ab', 'a', 'z'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.get_letter_guess(dummy_game)
    
    # It should only return the 'z' after rejecting the first three!
    assert result == 'z'
    
    

                
                
                
                