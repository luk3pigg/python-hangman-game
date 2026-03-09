import game_functions as gf
import time
import numpy as np

#additional ideas to focus on later:
#eventually, create word banks based on different lengths of words and ask user for input on which lenght they want
#adjust number of lives: difficulty setting
#adjust times/time depending on number ie 1 is time, times is 2+

#create a game score, based on lives, time taken, and length of word.
#tell them to take a break iftime exceeds a limit

#create a word bank (start with 6 letters)

word_bank = ['python', 'guitar', 'coffee', 'breeze', 'window', 'galaxy', 'jungle', 'silver', 'orchid', 'poetry']

#starting the game
total_session_games = 0
total_wins = 0
winning_times = []
game_active = gf.start_game()
game_start = time.time()
first_cycle = True
while game_active:   #loop for each session
    while first_cycle:
        chosen_word = gf.select_word(word_bank = word_bank)
        rules = input("Would you like to know the rules before we begin?\nYES: enter y\nNO: enter n\n\n")
        while True:
            if rules == 'y':
                print("These are the rules.\nOBJECTIVE: guess the secret word by guessing the letters it contains!\nYou will choose how many lives you have, and the length of the secret word.\nIf your letter guess is in the secret word, its location/s in the secret word will be revealed!\nBut be careful: if your letter guess is not in the secret word, you will lose a life.\nYou win the game if you guess all the letters and hence the word without losing all your lives!\n\nSo, without further ado....\n\n")
                first_cycle = False
                break
            elif rules == 'n':
                print("Cool.")
                first_cycle = False
                break
            else:
                rules = input("\nUnfortunately, that's an an invalid input. Please try again.\nYES: enter y\nNO: enter n\n\n").lower().strip()
    word_length = int(input("Please select how many letters you would like the secret word to have, between 5 and 10."))
    while True:
        if 5 <= word_length <= 10:
            break
        else:
            word_length = int(input("You have selected an invalid number of lives. Please select how many letters you would like the secret word to have, between 5 and 10."))
    lives = int(input("Please select how many lives you would like, between 5 and 10."))
    while True:
        if 5 <= lives <= 10:
            break
        else:
            lives = int(input("You have selected an invalid number of lives. Please select how many lives you would like, between 5 and 10."))
    #Initialisation
    correct_guesses = 0
    guessed_letters = []
    display_word = ['_'] * len(chosen_word)
    total_guesses = 0
    game_won = False
    start_time = time.time()
    while lives > 0 and not game_won: #loop for each individual game
        if total_guesses == 0:
            print("\nThe timer is on!")
            print("\nThis is your first guess!")
            print(f"\nYou currently have {lives} lives.")
            print("\nThis is the secret word:")
            print(*display_word)
        else:
            print("\n20 seconds have gone so far!")
            print(f"\nThis is guess number {total_guesses + 1}.")
            print(f"\nYou currently have {lives} lives.")
            print(f"\nYou currently have {correct_guesses} correct guesses.")
            print("\nYou have guessed the following letters:")
            print(*guessed_letters)
            print("\nHere's what you know so far:")
            print(*display_word)
        
        letter_guess, total_guesses = gf.letter_validation(total_guesses=total_guesses, guessed_letters=guessed_letters)
        lives, correct_guesses, game_won = gf.guess_result(guessed_letters, chosen_word, display_word, letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses, game_won=game_won)
    
        
    
    if game_won:
        end_time = time.time()
        time_elapsed = round(end_time - start_time, 0)
        winning_times.append(time_elapsed)
        average_time = np.mean(winning_times)
        total_wins += 1
        print(f"\n\nYou won! The secret word was {chosen_word}!")
        print(f"You took {time_elapsed} seconds.")
        if time_elapsed == min(winning_times) and len(winning_times) > 1:
            print("WOW! That's your fastest winning time yet!")
        print(f"Your average winning time is {average_time}!")
        #win percentage
        #average time taken for the wins
    else:
        print(f"Oh no! You have run out of lives! The correct word was {chosen_word}.")
        print("Better luck next time.")
    #stats
    total_session_games += 1
    session_duration = round(time.time() - game_start, 0)
    print(f"Total games you have played in this session: {total_session_games}")
    print(f"Total wins in this session: {total_wins}")
    print(f"Total session duration: {session_duration} seconds. Make sure you take a break soon!") # convert this into minutes, break if over 5 minutes!!
    #restart game option
    game_active = gf.restart_game()
    




