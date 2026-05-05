# Python Hangman Suite - Project Write-Up

## 1. Overview
*A brief summary of what the project is, the core technologies used, and your biggest wins (e.g., achieving 91% coverage on the logic engine, successfully porting the game to Streamlit).*




## 2. Core Engineering Concepts
*This is where you define the theory before showing the code.*
*   **Modularization:** Explain why breaking the monolith apart was crucial.
*   **Separation of Concerns & Decoupled Architecture:** Use the "Restaurant/Chef" analogy here to explain how the math engine is completely blind to the UI.
*   **State Management (OOP):** Discuss why using an Object (`HangmanGame`) made tracking lives and guessed letters cleaner than using loose variables.

## 3. Project Planning & Architecture
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
## 5. Key Lessons and Future Work
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