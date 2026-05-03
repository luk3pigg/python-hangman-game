# 🎮 Hangman Suite: A Multi-Interface Python Application

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_GUI-red)

A robust, multi-interface implementation of the classic Hangman game. 

This project was built using **professional software engineering principles**, featuring a decoupled architecture, allowing the game to be launched via Terminal, Desktop GUI, or Web Browser. The code was also unit tested using Pytest. 

*(Insert a screenshot or GIF of your game running here!)*

## ✨ Key Engineering Highlights
*   **Separation of Concerns:** Core game engine (`logic.py`) is completely decoupled from the User Interface (`terminal_main.py`) and entry point (`launcher.py`).
*   **Multi-Interface Ready:** Because the logic is decoupled, the same engine seamlessly powers a Terminal, Desktop, and Web app.
*   **Robust Testing:** Features automated unit and integration tests using `pytest` and `monkeypatch` to simulate user I/O.
*   **Environment Management:** Includes both `requirements.txt` (Pip) and `environment.yml` (Conda) for zero-friction local installation.

## 🎮 Core Features
*   **Customizable Difficulty:** Players can tailor the challenge by adjusting the length of the secret word and their starting number of lives.
*   **Intelligent Session Tracking:** The engine records performance across multiple rounds, calculating win percentages and average time-to-win.
*   **Bulletproof Input Handling:** Built-in safeguards catch typos, duplicate letter guesses, and invalid symbols, gracefully prompting the user without crashing the application.
*   **Multi-Interface Support:** Play via the classic Terminal, or test the underlying engine using the Desktop GUI or Web App. 

> **⚠️ Note on GUI & Web Apps:** The Desktop GUI and Streamlit Web App are currently included as *Proof of Concepts (Beta)*. Their primary purpose is to demonstrate the extensibility of the decoupled `logic.py` engine, proving the core math can be seamlessly ported to different frontend frameworks without rewriting the rules of the game.

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
git clone https://github.com/luk3pigg/python-hangman-suite.git
cd python-hangman-suite
pip install -r requirements.txt
```
**Using Conda:**
```bash
git clone https://github.com/luk3pigg/python-hangman-suite.git
cd python-hangman-suite
conda env create -f environment.yml
conda activate hangman-env
```

### 2. Launching the Suite
Run the launcher to access the main menu:
```bash
python launcher.py
```

From here, you can choose to launch the Classic Terminal Mode, the Desktop GUI, or the Web App.

## 🧪 Running the Tests
This project uses pytest for unit testing. To run the tests and generate an HTML coverage report:
```bash
pytest --cov=. --cov-report=html
```
Open htmlcov/index.html in your browser to view the interactive coverage breakdown.

---

## 🗺️ Future Roadmap
While the core engine is feature-complete and fully tested, there is always room for expansion. Future updates to this suite may include:
*   **Persistent Database:** Transitioning from temporary `SessionStats` to an SQLite or PostgreSQL database to track global high scores and player history across reboots.
*   **Dynamic Word Fetching:** Integrating a public Dictionary API to pull words and definitions dynamically, replacing the static `word_bank.json` file.
*   **Interface Feature Parity:** Upgrading the Beta GUI and Web App to have full feature parity with the heavily polished Terminal experience.



