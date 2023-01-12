import random
from words import words
import time
from colorama import Style

from colorama import init
from colorama import Fore, Style

# Initialize colorama
init()


def hangman_logo():
    """
    The word 'Hangman' is spelled out
    show the letters in blue at the beginning of the game.
    """


print(Fore.BLUE)
print("""
_    _
| |  | |
| |__| |  __ _  _ __    __ _  _ __ ___    __ _  _ __
|  __  | / _` || '_ \\  / _` || '_ ` _ \\  / _` || '_ \\
| |  | || (_| || | | || (_| || | | | | || (_| || | | |
|_|  |_| \\__,_||_| |_| \\__, ||_| |_| |_| \\__,_||_| |_|
                         __/ | slash
                        |___/
""".strip())
print(Fore.RESET)


def play_game():
    print("Welcome to Hangman!")
    time.sleep(0.5)
    print('Welcome to the hangman game!')


while True:
    name = input('What is your name? \n')
    if name.isalpha():
        break
    else:
        print('Please enter a valid name')

print('Hello,', name)

print(Style.BRIGHT + Fore.WHITE + "The game rules are simple:")
print("1.you have to guess a word one letter at a time.")
time.sleep(0.5)
print("2.If you guess a letter that is in the word, it will be revealed.")
time.sleep(0.5)
print("3.If you guess a letter that is not in the word, you lose a life.")
time.sleep(0.5)
print("You have 6 lives. Good luck!")
time.sleep(0.5)

# ASCII art images for hangman progress
HANGMAN_IMAGES = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Function set up the game in a randomly selected word,number of lives allowed


def setup_game(words, max_lives):
    word = random.choice(words)
    lives_allowed = max_lives
    return word, lives_allowed

# Main game loop


def play_hangman(word, lives_allowed):
    word = word.upper()
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()

    word_dict = {}
    for letter in word:
        word_dict[letter] = False

    lives = 0
    win = False
    print('\n' + HANGMAN_IMAGES[lives])
    while lives < lives_allowed:
        print('\nLives:', lives)
        print('Used letters:', ' '.join(used_letters))
        print('Word:', ' '.join(
            [letter if word_dict[letter] else '_' for letter in word]))

        user_letter = input('\nEnter a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_dict[user_letter] = True
                if all(word_dict.values()):
                    win = True
                    break
            else:
                lives += 1
                print('\n' + HANGMAN_IMAGES[lives])
        else:
            print('You have already used that letter.')

    if win:
        print("""\n {Fore.GREEN}Congratulations!{Style.RESET_ALL} You won!
        The word was {word}""")
        print(Fore.GREEN + '''
  _____
 /     \\
| () () |
 \\  ^  /
  |||||
  |||||
''' + Style.RESET_ALL)

    else:
        print(f'\n {Fore.RED}You lost!{Style.RESET_ALL} The word was {word}')
        print(Fore.RED + '''
  _____
 /     \\
|  X X  |
 \\     /
  |||||
  |||||
''' + Style.RESET_ALL)


# Set up the game with a list of words and the maximum number of lives allowed
max_lives = len(HANGMAN_IMAGES) - 1
word, lives_allowed = setup_game(words, max_lives)


# Start the game
play_again = 'y'
while play_again == 'y':
    play_hangman(word, lives_allowed)
    play_again = input("Do you want to play again? (Y/N)\n").lower()
    if play_again == 'n':
        print("Thanks for playing! Goodbye.")
        print(Fore.RED + '''
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|''')
        time.sleep(0.5)


def play_game():
    print("Welcome to Hangman")
