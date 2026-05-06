# Python Hangman Suite - Project Write-Up

## Table of Contents
* [Project Overview](#project-overview)
* [Key Concepts](#key-concepts)
* [Planning, Implementation, and Evolution](#planning-implementation-and-evolution)
    * [Planning](#planning)
    * [Implementation](#implementation)
    * [Evolution](#evolution)
* [Testing Strategy](#testing-strategy)
* [Code Highlights](#code-highlights)
    * [Decoupled Logic and Encapsulation](#decoupled-logic-and-encapsulation)
    * [Defensive UI Programming Using Robust Input Validation](#defensive-ui-programming-using-robust-input-validation)
    * [Simulating User I/O with pyest Mocking](#simulating-user-io-with-pytest-mocking)
* [Key Lessons and Future Work](#key-lessons-and-future-work)


## Project Overview

The aim of this project was to incorporate the fundamental programming concepts that I have learnt to build a functioning, interactive Python application with a decoupled logic backend and user interface. I achieved this by initially building a simple functions-based hangman game. I continuously increased its complexity by implementing production-level techniques such as robust error handling, Object-oriented Programming, and comprehensive unit testing. Ultimately, I engineered a decoupled core logic engine capable of running seamlessly across multiple interfaces. By documenting the complete software development lifecycle, this project serves as a foundational blueprint and standard for my future programming and engineering work. 

## Key Concepts 

To transition this project from a basic script to a production-ready application, I designed the architecture around three core software engineering principles:

*   **Modularisation:** Breaking a program down into distinct, single-purpose files, making code easier to read, debug, and scale. In this project, I modularise the code into `logic.py`, `terminal_utils.py`, `terminal_main.py`, and `launcher.py`.
*   **Decoupled Architecture:** Separating the logic/data layer from the User Interface (UI) to ensure the application appearance can be changed without breaking its functionality.
*   **State Management (OOP):** In complex, state-heavy applications, constantly passing loose variables between functions can be a major source of bugs and data corruption. Encapsulation solves this by bundling together the data and the functions permitted to modify them into a single 'Object'. In this project, I create `HangmanGame` and `SessionStats` classes to manage the game's state, resulting in cleaner, safer, and highly testable architecture. 

## Planning, Implementation, and Evolution

The development of the Hangman Suite followed a structured, iterative lifecycle. My priority was to ensure that the core logic was fully validated before introducing complex architectural patterns.

### Planning

Before writing a single line of executable Python, I mapped out a game loop for a Minimal Viable Product (MVP) using pseudocode written with comments. This allowed me to focus purely on the logic, without getting distracted by syntax or overwhelmed by different features I could add (e.g. anything UX related).

### Implementation

To build a functioning prototype, I intentionally kept the scope narrow:
*   **Static Data:** I started with a single, hardcoded secret word rather than a dictionary.
*   **Basic I/O:** I implemented a simple, functional loop to capture user guesses and print guess outcomes.
*   **The Monolith:** All logic (e.g. whether the guess was correct or not), state variables (e.g. `lives`), and terminal outputs were housed in a single script.

This MVP served as a crucial benchmark. It proved that the underlying game loop (evaluating correct vs. incorrect guesses) worked flawlessly.

Next, I began improving the efficiency, maintainability, and robustness of my code. 
*   **Data Externalisation:** I created a dictionary of 5 - 10 letter words and stored this as a separate JSON file. By decoupling the data layer from the application logic, I ensured that adding new words would never require altering the source code.
*   **Modularity:** I wrote functions to automate similar actions (e.g. asking yes/no questions, asking for a number within a certain range), then stored these in a separate file (`game_functions.py`) and imported them.
*   **Error Handling and Input Validation:** I engineered robust safety loops to trap invald inputs before they could crash the game or corrupt the game state. This included handling specific edge cases such as special characters, entering letter guesses longer than 1 character, and guessing the same letter twice.
*   **Decoupling the Logic and the UI:** I removed all `print()` statements and input validation loops from `game_functions.py` into helper functions at the top of `main.py`, because these functions tie code to a terminal envrionment. This kept `game_functions.py` interface independent. 
*   **Terminal User Experience:** I utilised OS-level commands to clear the terminal screen between round and introduce delays. Rather than allowing the terminal to become a messy, endlessly scrolling log of past guesses, this created a static, dynamically updating 'dashboard' that feels like a polished application.

This iterative approach of building a prototype and then refactoring it into isolated modules ensured that my architectural changes never broke the underlying logic, resulting in a highly stable program. This culminated in my first fully-functioning version 1 (instructions on how to run this version are in the **[`README.md`](README.md)**). 

### Evolution

With version 1 working perfectly, it was time to refactor the code into a production-grade application.

*   **Object-oriented Programming:** I replaced the loose state variables (e.g. `lives`) being passed in and out of functions with a dedicated `HangmanGame` class. This encapsulated the game's memory into a single instance, cleaning the program and making it easier to test. I also created a `SessionStats` class to manage data across different rounds; both were housed in `logic.py`. 
*   **Multiple Interfaces:** Due to the decoupled nature of `logic.py`, I was able to produce three different interfaces to run the game on (`terminal_main.py` for terminal, `gui_main.py` for desktop GUI, and `streamlit_app.py` for web app), without altering the core logic. 
*   **Professional Directory Organisation:** I moved the helper functions into a separate utlities file (`terminal_utils.py`) to create a clear `terminal_main.py` file, enforcing the principle of 'separation of concerns'. I also created an entry point (`launcher.py`) for the user to choose which interface they would like to play the game on. 

These edits culminated in version 2 of my code.

## Testing Strategy

Testing `logic.py` was crucial to ensure the engine was working before building additional user interfaces. I then focused on high-value unit tests for `terminal_utils.py`. 

### Testing the Core Engine (`logic.py`)

Testing the rules of the game was streamlined due to my use of Object-Oriented Programming. Because the game's state was securely encapsulated within the `HangmanGame` class, I did not need a user interface to test the core logic. I wrote targeted unit tests that simply instantiated a game object in the background, passed in a predefined secret word, and injected letters. I could then `assert` whether variables such as `lives` and `guessed_letters` updated correctly. This frictionless testing environment allowed me to achieve **91% test coverage** on the core logic engine.

### Simulating User I/O (`terminal_utils.py`)

Testing the logic in the terminal UI presented an engineering challenge: functions using Python's built-in `input()` command will permanently pause an automated test suite while waiting for a human to type on the keyboard. To solve this, I used `pytest`'s built-in `monkeypatch` feature. This allowed me to simulate a user typing numbers, special symbols, and duplicate letters, verifying that my error-handling loops correctly trapped invalid data and prompted the user again, all without ever freezing the test suite. I decided to write tests exclusively for these error-handling loops, resulting in a targeted **30% test coverage**. The remaining untested lines were either built-in functions or code that relied on `logic.py`, which had already been tested.


## Code Highlights 

### Decoupled Logic and Encapsulation

The most significant architectural improvement in this project was migrating the core game loop from functional programming to an Object-oriented approach. 

In my initial version (V1), tracking the game state required passing multiple loose variables in and out of every single function, which was prone to data corruption and difficult to test. Furthermore, core logic was entangled with the user interface via hardcoded `print()` statements:

**Before: The Functional Approach (V1)**

*File: `hangman_v1_functional/main.py`*

```python
# State relies on loose variables passed back and forth
lives, correct_guesses, game_won = gf.guess_result(guessed_letters=guessed_letters, chosen_word=chosen_word, display_word=display_word, letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses, game_won=game_won)  
            
# --- Turn Feedback ---
if letter_guess in chosen_word:
    occurrences = chosen_word.count(letter_guess)
    # Hardcoding print() here couples the logic to the terminal, 
    # making this part completely unusable for a Web or GUI app.
    print("Correct guess!")
    time.sleep(1.0)
    if occurrences == 1:
        print("\nYour guess appears in the secret word once.")
    else:   
        print(f"\nYour guess appears in the secret word {occurrences} times!")
        time.sleep(1.0)
else:
    print("Incorrect guess...Unlucky!")
    time.sleep(1.0)
```

By refactoring the engine into the HangmanGame class below, the game now securely remembers its own state. Notice how the refactored method requires only a single argument (`letter_guess`), as the data layer (`self.lives`, `self.guessed_letters` etc) is completely encapsulated. Also, this method communicates with the UI by returning a tuple (bool, int). This maintains strict decoupling; the engine calculates the occurrences, but leaves the actual printing to the interface layer:

*File: `hangman_v2_oop/logic.py`*

```python
class HangmanGame:
    # ... [__init__ and other methods hidden for brevity] ...
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
        # The object manages its own memory securely
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
            
            # Returning pure data (a tuple) instead of strings ensures 
            # this engine remains completely blind to the UI layer.
            return True, occurrences
        else:
            self.lives -= 1
            return False, 0
```

Because the logic is now encapsulated and clean, the implementation in the Terminal UI becomes drastically shorter and easier to read.
Notice how the engine object is instantiated in the main setup file, but the actual evaluation happens inside the clean utility loop:

*File: `hangman_v2_oop/terminal_main.py`*

```python
game = HangmanGame(chosen_word=chosen_word, starting_lives=lives) #instantiating the object
```

**After: The OOP Approach (V2)**

*File: `hangman_v2_oop/terminal_utils.py`*
```python
# The UI simply passes the user's letter guess and interprets the tuple response
is_correct, occurrences = game.evaluate_guess(letter_guess)
if is_correct:
            print("Correct guess!")
            time.sleep(1.0)
            if occurrences == 1: print("\nYour guess appears in the secret word once.")
            else: print(f"\nYour guess appears in the secret word {occurrences} times!")
            time.sleep(1.0)
        else:
            print("Incorrect guess...Unlucky!") 
            time.sleep(1.0)
```

### Defensive UI Programming Using Robust Input Validation

Because the core logic engine expects clean data, the interface layer must act as a filter. To eliminate redundant code and prevent edge-case crashes, I engineered a "dynamic prompting" pattern for all `while` loops that handle user I/O. 

Rather than trapping the user in a nested hierarchy of `input()` requests, the prompt string is initialised outside the loop and dynamically reassigned if validation fails. This ensures the user is provided with clean, relevant error messages that avoid repetition.

**Example 1: Trapping Type Errors**

This utility ensures the user inputs a valid integer when selecting parameters like starting lives. By dynamically updating the `prompt` variable instead of requesting new input inside the `except` block, the user is continually fed through the exact same `try/except` safety net, completely preventing application crashes if a user inputs consecutive invalid data types. This highlights the strength of my chosen approach. 

*File: `hangman_v2_oop/terminal_utils.py`*

```python
def input_within_range(lower, upper, prompt, subject):
    """
    Forces the user to input a valid integer within a specified range.
    
    Args:
        lower (int): Minimum acceptable value.
        upper (int): Maximum acceptable value.
        prompt (str): The initial prompt text.
        subject (str): Contextual label for error messages (e.g., 'lives').
        
    Returns:
        user_input (int): The validated user input.
    """
    while True:
        try:
            # The safety net resets at the top of every loop iteration
            user_input = int(input(prompt))
            if lower <= user_input <= upper:
                return user_input 
            else:
                # Dynamically update the prompt with a contextual out-of-bounds error
                prompt = (f"\n[!] That is not within the specified range for the {subject}. Please enter a number between {lower} and {upper} inclusive.\n> ")
        except ValueError:
            # Dynamically update the prompt with a type error message
            prompt = (f"\n[!] That is not a valid number. Please enter a valid {subject} between {lower} and {upper} inclusive.\n> ")
```

**Example 2: Delegating Validation Logic**

This snippet highlights the strict separation of concerns within my suite. While the UI handles the physical while loop, it does not actually know why a letter guess is invalid (e.g., duplicate letter, special character). It simply queries the decoupled engine (game.is_valid_guess) and renders the resulting error string.

*File: `hangman_v2_oop/terminal_utils.py`*

```python
def get_letter_guess(game):
    """
    Prompts the user for a valid, single letter that hasn't been guessed yet.
    
    Args:
        game (HangmanGame): The current active instance of the Hangman game.
        
    Returns:
        str: A validated, lowercase, single-character string.
    """
    #Assigns the initial prompt
    prompt = "\nPlease enter a letter guess:\n>  " 
    while True:
        letter_guess = input(prompt).lower().strip()
        
        # The UI remains "dumb" by delegating logic back to the engine
        is_valid, error_msg = game.is_valid_guess(guess=letter_guess)
        
        if is_valid:
            return letter_guess 
        else:
            # The engine provides the specific error message to display through reassignment
            prompt = f"\n[!] {error_msg} Please try another guess:\n> "

```

### Simulating User I/O with pytest Mocking

As discussed in the Testing Strategies section, any function containing `input()` commands will permanently pause an automated test suite.

To solve this, I used Pytest's built-in `monkeypatch` feature. The following snippet demonstrates how I injected an array of simulated keystrokes to intentionally feed the function invalid data. The `try/except` safety loops caught the errors without crashing the test suite, and the test passed when the single valid input (6) was finally inputted.

*File: `hangman_v2_oop/tests/test_terminal_utils.py`*

```python
def test_input_within_range_recovers_from_errors(monkeypatch):
    """
    Sad Path: Tests that the function rejects strings (ValueError) 
    and out-of-bounds numbers before finally accepting a valid input.
    """
    # 1. Define the simulated user behavior (Type Error -> Out of Bounds -> Success)
    fake_keyboard = iter(['apple', '99', '6'])
    
    # 2. monkeypatch intercepts the built-in input() command, preventing the 
    # test suite from freezing by injecting our simulated keystrokes instead.
    monkeypatch.setattr('builtins.input', lambda prompt: next(fake_keyboard))

    # 3. Execute the function. It silently processes the two bad inputs, 
    # updates the prompt dynamically, and finally returns the '6'.
    result = ui.input_within_range(5, 10, "Pick a number", "test")
    
    # 4. Asserting the final state proves the safety loop successfully 
    # recovered from consecutive errors without raising an exception.
    assert result == 6
```

---

## Key Lessons and Future Work

Building the Hangman Suite was a pivotal step in transitioning from simply writing code to engineering software. It reinforced the importance of planning, architecture, and quality assurance. Below are just some of the key lessons I learnt and my ideas for future work. 

### 6.1 Key Engineering Takeaways

*   **The Software Development Life Cycle (SDLC):** This project bridged the gap between being an intermediate coder and a systems thinker. By adhering to a SDLC (planning with pseudocode, building a Minimum Viable Product (MVP), and systematically refactoring), I learned how to build a comprehensive suite using professional conventions rather than just brain-dumping a monolithic script.
*   **The Strength of Decoupled Architecture:** Forcing my game engine to be completely "blind" to the user interface was a challenging but rewarding part of this project. It taught me how separating concerns makes a codebase much more scalable e.g. by introducing different user interfaces.
*   **The Value of Proof of Concepts (PoC):** I learned that building an initial functions-based prototype (V1) was not a waste of time, rather serving as a vital PoC that validated the core logic. My desktop GUI and web app PoCs also justified my architectural decisions made throughout, demonstrating the scalability of this project.
*   **Context-Dependent User Experience (UX):** Expanding the game to three distinct interfaces taught me that UX strategies are not one-size-fits-all. A terminal requires dynamic prompting and OS-level screen clearing, whereas a web application requires navigation through different screens and aesthetic visual feedback.

### 6.2 Future Roadmap

While the core suite is highly stable, the decoupled architecture leaves the door open for several exciting expansions:
*   **API Integration:** I plan to replace the static `word_bank.json` file with a live web API. This will provide a much larger word bank without increasing the repository size, and will allow the game to fetch real-time definitions to present to the user upon game completion.
*   **Dynamic Scoring Engine:** I intend to expand the `HangmanGame` logic to calculate a weighted score upon victory. By factoring in the number of lives preserved and the length of the secret word, I can introduce a highly replayable, competitive edge to the core loop.
*   **Database Persistence & Leaderboards:** Currently, the `SessionStats` class only tracks data for a single runtime session. By integrating a relational database (such as SQLite or PostgreSQL), I can make player profiles persistent, allowing for historical win-rate tracking and global leaderboards.
*   **Advanced UI/UX and Asset Rendering:** I plan to deepen my knowledge in Tkinter and Streamlit to introduce dynamic graphical assets. Specifically, I will map the `self.lives` state to a visual rendering of a Hangman figure, creating a more engaging frontend experience that goes beyond text-based feedback.
