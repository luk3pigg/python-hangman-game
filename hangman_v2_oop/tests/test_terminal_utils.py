import terminal_utils as ui  
from logic import HangmanGame

# ==========================================
# TESTS FOR get_yes_no_input
# ==========================================

def test_yes_no_input_accepts_yes(monkeypatch):
    """Happy Path: Tests that typing 'y' immediately returns True."""
    
    monkeypatch.setattr('builtins.input', lambda prompt: 'y')
    
    result = ui.get_yes_no_input("Are you ready?")
    assert result == True
    
def test_yes_no_input_recovers_from_invalid(monkeypatch):
    """Sad Path: Tests that typing nonsense is rejected until 'n' is typed."""
    
    fake_keyboard = iter(['maybe', 'idk', '!', '47', 'N', 'no', 'n'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.get_yes_no_input("Are you ready?")
    assert result == False
    
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
    
    fake_keyboard = iter(['apple', '99', '6'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.input_within_range(5, 10, "Pick a number", "test")
    assert result == 6
    
# ==========================================
# TESTS FOR get_letter_guess
# ==========================================

def test_letter_input_returns_letter(monkeypatch):
    """Happy Path: Tests that a valid letter is accepted immediately."""
    
    dummy_game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    monkeypatch.setattr('builtins.input', lambda prompt: 'G') #works for both G and g
    
    result = ui.get_letter_guess(dummy_game)
    
    assert result == 'g'
    
def test_letter_input_rejects_bad_guesses(monkeypatch):
    """
    Sad Path: Tests that the function rejects numbers, multiple letters, 
    and already-guessed letters before finally accepting a valid new letter.
    """
    dummy_game = HangmanGame(chosen_word="apple", starting_lives=5)
    
    dummy_game.guessed_letters.append('a')
    
    fake_keyboard = iter(['1', 'ab', 'a', 'z'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))
    
    result = ui.get_letter_guess(dummy_game)
    
    assert result == 'z'
    
    

                
                
                
                