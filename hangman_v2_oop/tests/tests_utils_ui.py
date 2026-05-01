import pytest
import utils_ui as ui  # Change this if your file is named utils_ui.py

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

