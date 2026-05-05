# Python Hangman Suite - Project Write-Up

## Table of Contents
* [Project Overview](#project-overview)
* [Concepts and Highlights](#2-concepts-and-highlights)
* [Planning, Implementation, and Evolution]
* [Planning](#planning)
* [Implementation](#implementation)
* [Evolution](#Evolution)
* [Testing](#testing)

## Project Overview

Is this a good strcuture:

1.) Overview

2.) Key concepts 

3.) Planning, Implementation, and Evolution

4.) Testing

5.) Code Highlights (and game features and flowchart)

6.) Lessons learned and future work


The aim of this project was to incorporate the fundamental programming concepts that I have learnt to build a functioning, interactive Python application with a decoupled logic backend and user interface. I achieved this by initially building a simple hangman game based on functions. I continuously increased its complexity by implementing production-level techniques such as robust error handling, Object-oriented Programming, and comprehensive unit testing. Ultimately, I engineered a decoupled core logic engine capable of running seamlessly across multiple interfaces. By documenting the complete software development lifecycle, this project serves as a foundational blueprint and standard for my future programming and engineering work. 


## 2. Key Concepts 


*   **Modularization:** Explain why breaking the monolith apart was crucial.
*   **Separation of Concerns & Decoupled Architecture:** Use the "Restaurant/Chef" analogy here to explain how the math engine is completely blind to the UI.
*   **State Management (OOP):** Discuss why using an Object (`HangmanGame`) made tracking lives and guessed letters cleaner than using loose variables.



To transition this project from a basic script to a production-ready application, I redesigned the architecture around three core software engineering principles:

talk about SDLC too!

User experience (UX)

User Interface (UI)

### Modularization (Breaking the Monolith)
Initially, the game existed as a monolithic script where game logic, state tracking, and terminal `print()` statements were tightly intertwined. I modularized the codebase by splitting it into distinct files (`logic.py`, `terminal_utils.py`, and `launcher.py`). This prevented "spaghetti code" and ensured that a change to the text formatting would not accidentally break the core mathematical rules of the game.

### Separation of Concerns & Decoupled Architecture
Beyond just splitting files, I ensured the modules were strictly decoupled. 
*   **The Engine (`logic.py`):** Acts as the "Chef." It exclusively handles the mathematical state (lives remaining, win/loss conditions). It is completely "blind" to the user interface.
*   **The Interface (`terminal_utils.py`):** Acts as the "Waiter." It exclusively handles formatting text, clearing screens, and trapping invalid user inputs in safety loops.

Because they only communicate through strict function arguments (like passing a verified letter to the engine), the core logic can be seamlessly plugged into completely different frontend frameworks (like Streamlit or a Desktop GUI) without rewriting any game rules.

### Encapsulation via Object-Oriented Programming (OOP)
In the initial functional version of the game, managing state required passing multiple loose variables (e.g., `current_lives`, `guessed_letters`, `chosen_word`) between every function. By refactoring the engine into a `HangmanGame` class, I utilized OOP to **encapsulate** these variables. The object securely remembers its own state, making the code much cleaner to read and drastically easier to isolate and test using Pytest.

## Planning, Implementation, and Evolution

The development of the Hangman Suite followed a structured, iterative lifecycle. My priority was to ensure that the core logic was fully validated before introducing complex architectural patterns.

### Planning

Before writing a single line of executable Python, I mapped out a game loop for a Minimal Viable Product (MVP) using pseudocode written with comments. This allowed me to focus purely on the logic, without getting distracted by syntax or overwhelmed by different features I could add (e.g. anything UX related).

### Implementation

To build a functioning prototype, I intentionally kept the scope narrow:
*   **Static Data:** I started with a single, hardcoded secret word rather than a dictionary.
*   **Basic I/O:** I implemented a simple, functional loop to capture user guesses and print results.
*   **The Monolith:** All logic, state variables, and terminal outputs were housed in a single script.

This MVP served as a crucial benchmark. It proved that the underlying game loop (evaluating correct vs. incorrect guesses) worked flawlessly.

Next, I began improving the efficiency, maintainability, and robustness of my code. 
*   **Data Externalisation:** I created a dictionary of 5 - 10 letter words and stored this as a separate JSON file for the code to access, to allow for scalability. 
*   **Modularity:** I wrote functions to automate similar actions (e.g. asking yes/no questions, asking for a number within a certain range), then stored these in a separate file (`game_functions.py`) and imported them.
*   **Error Handling and Input Validation:** I engineered robust safety loops to trap invald inputs before they could crash the game or corrupt the game state. This included handling specific edge cases such as special characters, entering letter guesses longer than 1 character, and guessing the same letter twice.
*   **Decoupling the Logic and the UI:** I removed all `print()` statements and input validation loops from `game_functions.py` into helper functions at the top of `main.py`.
*   **Terminal User Experience:** I utilised OS-level commands to clear the terminal screen between round and introduce delays to polish the game. 

This iterative approach of building a prototype and then refactoring it into isolated modules ensured that my architectural changes never broke the underlying logic, resulting in a highly stable program. This culminated in my first fully-functioning version 1 (instructions on how to run this version are in the **[`README.md`](README.md)**). 

### Evolution

With this version working perfectly, it was time to refactor the code into a production-grade application.

*   **Object-oriented Programming:** I replaced the loose state variables (e.g. `lives`) being passed in and out of functions with a dedicated `HangmanGame` class. This encapsulated the game's memory into a single instance, cleaning the program and making it easier to test. I also created a ...class; both were writte/stored? were written in `logic.py`. 
*   **Multiple Interfaces:** Due to the decoupled nature of `logic.py`, I was able to produce three different interfaces to run the game on (`terminal_main.py` for terminal, `gui_main.py` for desktop GUI, and `streamlit_app.py` for web app), without altering `logic.py`. 
*   **Professional Directory Organisation:** I moved the helper functions into a separate utlities file (`terminal_utils.py`) to create a clear `terminal_main.py` file, enforcing the principle of 'separation of concerns'. I also created an entry point (`launcher.py`) for the user to choose which interface they would like to play the game on. 

## Testing







*Explain your initial approach.*
*   Why did you decide to build the `logic.py` file first before ever touching a `print()` statement?
*   Include a brief explanation of how `terminal_utils.py` acts as the safety net for user inputs.

## 4. Application Implementation & Key Code Snippets
*Don't paste the whole file! Just highlight the clever parts.*

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

---

## 🏗️ Architecture & Engineering Decisions

### 1. Separation of Concerns (The Restaurant Analogy)
To ensure the codebase remained scalable and testable, the code is heavily modularized:
*   **The Chef (`logic.py`):** The core engine. It handles all mathematical states, win/loss conditions, and memory. It contains zero UI logic and is completely "blind" to how the user is playing.
*   **The Waiter (`terminal_utils.py`):** The UI layer. It exclusively handles formatting text, clearing screens, and trapping invalid user inputs in safety loops.
*   **The General Manager (`terminal_main.py`):** The orchestrator. It manages the high-level game phases, loading the JSON word bank, and passing data between the UI and the Engine.

### 2. Strategic Test Coverage
If you review the test suite, you will notice `logic.py` has near-perfect coverage, while `terminal_utils.py` coverage is deliberately lower (around ~31%). 

This split is entirely by design: **prioritizing business logic over I/O side effects.**
Automating tests for `print()` statements and `time.sleep()` offers zero Return on Investment. The test suite aggressively targets the isolated mathematical engine, state memory, and complex user-input validation (using `monkeypatch`), demonstrating a pragmatic approach to QA rather than chasing vanity metrics.

---