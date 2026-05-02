import subprocess
import sys
import os

def clear_screen():
    # Clears the terminal screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
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
    clear_screen()
    while True:
        
        try:
            print_menu()
            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                clear_screen()
                print("\n🚀 Launching Terminal Mode...\n")
                subprocess.run([sys.executable, "main.py"])
                
            elif choice == '2':
                print("\n🚀 Launching Desktop GUI...\n")
                subprocess.run([sys.executable, "gui_main.py"])
                
            elif choice == '3':
                print("\n🚀 Launching Web App...\n\n\n(Press Ctrl+C in this terminal to stop the server later)\n")
                subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
                
            elif choice == '4':
                clear_screen()
                print("\nThanks for playing! Goodbye.\n")
                break
                
            else:
                clear_screen()
                print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            # This catches Ctrl+C no matter which app is currently running!
            clear_screen()
            print("\n\n🛑 Process interrupted safely. Returning to main menu...")
            # The loop automatically restarts and shows the menu again.

if __name__ == "__main__":
    launch_game()