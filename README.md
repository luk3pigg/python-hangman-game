# 🎮 Python Hangman Project

## A modular hangman game built in Python, featuring customisable difficulty and a speedrun timer.

## 🔗 Repository Link
[Check out the main project repository here](https://github.com/luk3pigg/python-hangman-game)

## ✨ Features
* Modular Architecture: Game logic is separated into main.py and game_functions.py for better maintainability.
* Dynamic Difficulty: Players can select their preferred word length and number of lives to customise difficulty. 
* Robust Input Validation: Uses try/except blocks to handle invalid inputs without crashing.
* Game Timer: Tracks exactly how long each successful attempt takes.

## 📂 Project Structure
* `main.py`: The entry point of the game. Contains the main game loop and user interface logic.
* `game_functions.py`: The engine containing core logic, word selection, and input validation.
* `README.md`: Project documentation.

## 🚀 How to Run
1. Clone the repository:
```git clone https://github.com/luk3pigg/python-hangman-game```

2. Run the game in your preferred IDE: ```main.py```

## 📖 How to Play
* **OBJECTIVE**: guess the secret word by guessing the letters it contains.
* Choose how many lives you have, and the length of the secret word.
* If your letter guess is in the secret word, its location/s in the secret word will be revealed.
* But be careful: if your letter guess is not in the secret word, you will lose a life.
* You win the game if you guess all the letters and hence the word without losing all your lives!

## 🛠️ Built With
* Python
* Spyder IDE
* Git/GitHub for version control

Last updated: 09/03/26
