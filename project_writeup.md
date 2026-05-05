# Python Hangman Suite - Project Write-Up

## Table of Contents
* [Project Overview](#project-overview)
* [Key Concepts](#key-concepts)
* [Planning, Implementation, and Evolution](#planning-implementation-and-evolution)
    * [Planning](#planning)
    * [Implementation](#implementation)
    * [Evolution](#evolution)
* [Testing](#testing)
* [Code Highlights](#code-highlights)
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

## Testing

Testing `logic.py` was crucial to ensure the engine was working before building additional user interfaces. I then focused on high-value unit tests for `terminal_utils.py`. 

### Testing the Core Engine (`logic.py`)

Testing the rules of the game was streamlined due to my use of Object-Oriented Programming. Because the game's state was securely encapsulated within the `HangmanGame` class, I did not need a user interface to test the core logic. I wrote targeted unit tests that simply instantiated a game object in the background, passed in a predefined secret word, and injected letters. I could then `assert` whether variables such as `lives` and `guessed_letters` updated correctly. This frictionless testing environment allowed me to achieve **91% test coverage** on the core logic engine.

### Simulating User I/O (`terminal_utils.py`)

Testing the logic in the terminal UI presented an engineering challenge: functions using Python's built-in `input()` command will permanently pause an automated test suite while waiting for a human to type on the keyboard. To solve this, I used `pytest`'s built-in `monkeypatch` feature. This allowed me to simulate a user typing numbers, special symbols, and duplicate letters, verifying that my error-handling loops correctly trapped invalid data and prompted the user again, all without ever freezing the test suite. I decided to write tests exclusively for these error-handling loops, resulting in a targeted **30% test coverage**. The remaining untested lines were either built-in functions or code that relied on `logic.py`, which had already been tested.


## Code Highlights 


game features and flowchart







### The Decoupled Engine
Here is how the game evaluates a guess without needing to know if the user is in a terminal or on a web page:
```python
# (Paste a 5-10 line snippet of your evaluate_guess function here)
 ```

### Bulletproof Input Validation
Here is how the UI layer catches bad inputs before they ever reach the game engine:
```python
# (Paste a snippet of your while-loop or try-except block here)
 ```










## Key Lessons and Future Work
*Don't paste the whole file! Just highlight the clever parts.*


Lessons Learned
Strategic Testing: Explain your realization that testing pure logic (91% coverage) provides massive ROI, while testing I/O (print statements) is a waste of resources.

The Value of Proof of Concepts: Discuss what you learned by building the Streamlit app—how it validated your decoupled architecture.

Future Scope
Mention adding a database (SQLite/PostgreSQL) for persistent SessionStats.

Mention integrating a live Dictionary API to replace the static JSON file.
Since we already have the concepts (like decoupling and testing strategy) fresh in our minds, **which section of this write-up would you like to draft first?** We can start with the "Overview of Concepts" and get those engineering definitions locked in, or we can pick the best code snippets for section 4.



Key lessons - SDLC! what it actually means are what the stages are, how I can use this in future proejcts 

Importance of user experience
Testing - had never come acrssos formally before
