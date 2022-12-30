import random
from words import words

from time import sleep
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

import random



# Choose a random word
word = random.choice(words)

# Initialize variables
guesses = []
max_guesses = 8
current_guesses = 0

# List of images for different stages of the game
images = [
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
print("Welcome to Hangman!")
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
        print("Congratulations! You won!")
        break
    elif current_guesses >= max_guesses:
        print("Sorry, you lost. The word was:", word)
        break

    # Get the player's guess
    guess = input("Guess a letter: ")
    guesses.append(guess)
    current_guesses += 1

    # Display the current image
    print(images[current_guesses])
