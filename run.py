import random
from words import words
import time
import string

# For using coloured text in the terminal
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def get_valid_word(words):
    word = random.choice(words)
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        return word
# Choose a random word
word = random.choice(words)

# Initialize variables
guesses = []
max_guesses = 6
current_guesses = 0

def hangman_logo():
    """
    The word 'Hangman' is spelled out
    show the letters in blue at the beginning of the game.
    """

print(Fore.BLUE + """
 
  _   _                                               _____                 _    _     _     
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __       |  ___|__  _ __       / \  | |   | |    
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ _____| |_ / _ \| '__|____ / _ \ | |   | |    
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |_____|  _| (_) | | |_____/ ___ \| |___| |___ 
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     |_|  \___/|_|      /_/   \_\_____|_____|
                    |___/                                                                    

   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  \n
""")

#display the Hangman image based on the number of lives remaining
images = [Fore.RED +
    """
    +---+
        |
        |
        |
       ===""",
    """
    +---+
    O   |
        |
        |
       ===""",
    """
    +---+
    O   |
    |   |
        |
       ===""",
    """
    +---+
    O   |
   /|   |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
    """
    +---+
    O   |
   /|\  |
   / \  |
       ===""",
]

# Display the initial state of the game
print(images[0])
def welcome_page():
    """
   Welcome user to the game
   Ask the user name
   """ 

print(Fore.BLUE + 'Welcome to Hangman For All')
# Get the player's name
player_name = input(Fore.GREEN + "What is your name?\n")
# Print a message to the player
print(Fore.BLUE + f"Hello, {player_name}! Let's play Hangman For All!")
print(Fore.BLUE + f"Good Luck on Your Game!")
print(f"You have {max_guesses} guesses to guess the word.")


# Main game loop
while True:
    # Print the current state of the word
    current_word = ""
    for letter in word:
        if letter in guesses:
            current_word += letter
        else:
            current_word += "_"
    print(current_word)

    # Check if the player has won or lost
    if current_word == word:
        print(Fore.YELLOW + "Congratulations! You won!")
        break
    elif current_guesses >= max_guesses:
        print(Fore.RED + "Sorry, You lost! The word was:", word)
        break
      # Pause the game for 1 second
    time.sleep(1)

    # Get the player's guess
    guess = input("Guess a letter:\n")
    guesses.append(guess)
    current_guesses += 1

    # Display the current image
    print(images[current_guesses])


    
    

# Play the game
while True:
    hangman()

    # Ask the player if they want to play again
   
    print(play_again)("\nDo you want to play again? (Y/N) ")
    if play_again.lower() != "y":
        break

