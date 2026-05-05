# 🎮 Hangman Suite: A Multi-Interface Python Application

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_GUI-red)

A robust, multi-interface implementation of the classic Hangman game. 

This project was built using **professional software engineering principles**, featuring a decoupled architecture, unit testing using Pytest, and multiple interfaces to run the game engine on.  

*(Insert a screenshot or GIF of your game running here!)*

---

Please read **[`project_writeup.md`](project_writeup.md)** for a deeper analysis of this project.

---


## ✨ Key Engineering Highlights 
*   **Object-Oriented Programming:** Encapsulated game states, such as remaining lives and guessed letters, into manageable and testable objects. 
*   **Decoupled Architecture:** Separated the game engine (`logic.py`) to facilitate development of multiple independent user interfaces. The user selects their mode in(`launcher.py`).
*   **Robust Testing:** Features unit tests on the logic using `pytest` with 91% coverage. Used `monkeypatch` to simulate user I/O to test the terminal interface.
*   **Learning Journey:** Included initial function-based version (v1) of the game to benchmark progress.

> **⚠️ Note on GUI & Web Apps:** The Desktop GUI and Streamlit Web App are currently included as *Proof of Concepts (Beta)*. Their primary purpose is to demonstrate the extensibility of the decoupled `logic.py` engine.

## 🎮 Game Features
*   **Customisable Difficulty:** Players can choose the length of the secret word and their starting number of lives.
*   **Intelligent Game Tracking:** If a game is won, the engine records the time taken to guess the secret word, the average winning time of all games played by the user, and a bonus message if the game was their quickest winning time yet.
*   **Intelligent Session Tracking:** The engine records the total playing duration, the number of wins in the session, and the % win rate.
*   **Robust Input Handling:** Built-in safeguards to catch typos, duplicate letter guesses, and invalid symbols, prompting the user without crashing the application.

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
cd hangman_v2_oop/
python launcher.py
```

From here, you can choose to launch the Classic Terminal Mode, the Desktop GUI, or the Web App.

### 🕰️Exploring function-based version (v1)
To demonstrate the evolution of this project, the initial version has been preserved. It can be run as follows:
```bash
cd hangman_v1_functional/
python main.py
```
---

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



