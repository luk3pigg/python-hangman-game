# 🎮 Hangman Suite: A Multi-Interface Python Application

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green)
![Coverage](https://img.shields.io/badge/Coverage-Strategic-success)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_GUI-red)

A robust, multi-interface implementation of the classic Hangman game. 

This project was built using **professional software engineering principles**, featuring a decoupled architecture, comprehensive test coverage, and a unified launcher that serves the game via Terminal, Desktop GUI, or Web Browser.

*(Insert a screenshot or GIF of your game running here!)*

## ✨ Key Engineering Highlights
*   **Separation of Concerns:** Core game engine (`logic.py`) is completely decoupled from the User Interface (`terminal_utils.py`) and the Orchestrator (`main.py`).
*   **Multi-Interface Ready:** Because the logic is decoupled, the same engine seamlessly powers a Terminal, Desktop, and Web app.
*   **Robust Testing:** Features automated unit and integration tests using `pytest` and `monkeypatch` to simulate user I/O.
*   **Environment Management:** Includes both `requirements.txt` (Pip) and `environment.yml` (Conda) for zero-friction local installation.

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

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies using your preferred package manager:

**Using Pip:**
```bash
git clone [https://github.com/luk3pigg/python-hangman-suite.git](https://github.com/luk3pigg/python-hangman-suite.git)
cd hangman-suite
pip install -r requirements.txt
```
**Using Conda:**
```bash
git clone [https://github.com/luk3pigg/python-hangman-suite.git](https://github.com/luk3pigg/python-hangman-suite.git)
cd hangman-suite
conda env create -f environment.yml
conda activate hangman-env
```

### 2. Launching the Suite
Run the launcher to access the main menu:
```bash
python launcher.py
```

From here, you can choose to launch the Classic Terminal Mode, the Desktop GUI, or the Web App.

## 🧪 Running the Test Suite
This project uses pytest for unit testing. To run the tests and generate an HTML coverage report:
```bash
pytest --cov=. --cov-report=html
```
Open htmlcov/index.html in your browser to view the interactive coverage breakdown.





