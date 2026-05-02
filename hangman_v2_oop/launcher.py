import subprocess
import sys
import os
import time 

def clear_screen():
    """Clears the terminal scrollback depending on the host OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """
    Displays the main launcher menu with interface options.
    """
    print("\n" + "="*40)
    print("      H A N G M A N : S U I T E     ")
    print("="*40)
    print("How would you like to play today?\n")
    print("  [1] Terminal Mode (Classic)")
    print("  [2] Desktop GUI Mode - BETA PREVIEW")
    print("  [3] Web App Mode - BETA PREVIEW")
    print("  [4] Exit")
    print("="*40)

def launch_game():
    """
    Runs the continuous launcher loop, handling user input and 
    spawning subprocesses for the selected game interfaces."""
    clear_screen()
    while True:
        
        try:
            print_menu()
            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                clear_screen()
                print("\n🚀 Launching Terminal Mode...\n")
                subprocess.run([sys.executable, "terminal_main.py"])
                
            elif choice == '2':
                print("\n🚀 Launching Desktop GUI...\n")
                subprocess.run([sys.executable, "gui_main.py"])
                
            elif choice == '3':
                print("\n🚀 Launching Web App...\n\n\n(Press Ctrl+C in this terminal to stop the server later)\n")
                subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
                
            elif choice == '4':
                clear_screen()
                print("\nThanks for playing! Goodbye.\n")
                sys.exit(0)
                
            else:
                clear_screen()
                print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Process interrupted safely. Returning to main menu...")
            time.sleep(1.5)
            clear_screen()
        

if __name__ == "__main__":
    try:
        launch_game()
    except KeyboardInterrupt:
        clear_screen()
        print("\nLauncher aborted. Goodbye!\n")
        sys.exit(0)