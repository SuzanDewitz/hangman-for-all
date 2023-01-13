# HANGMAN-For-ALL
  *HANGMAN for aLL is a Python terminal game, which runs on the Code Institute mock terminal on Heroku.The play_game function prints out some introductory messages
 to the user and describes the rules of the game. The game is played by guessing letters in a secret word, one at a time. If a letter 
 is in the word, it is revealed, but if the letter is not in the word, the player loses a life. The player has six lives to guess the 
 word before the game is over.
 * Hangman is a great game for spelling and vocabulary knowledge to recognize how letters fit together.The hangman game is a word guessing game that is typically used to teach or reinforce spelling and vocabulary skills. In the game, players are presented with a word or phrase and must guess the letters that make up that word or phrase before a "hangman" is fully drawn.
 <br>
 <br>
  ![amiresposive](images/hangman%20ami%20responsive.png)
 <br>
 <br>
 <br>







  ![amiresposive](images/hangman%20image%20removed%20erorr.jpg)

 <br>
 <br>
 <br>

# Table of Contents
## Home
## How to play
## Design
## Features and user experience 
 
## Tecnologies used
## Fixed and unfixed bugs
## Validation
## Testing
## Project creation and deployment
## Credits
 <br>
 <br>
 <br>


Hangman-For-All
# Home
## How to play
  * This is a Python script that implements a simple game of Hangman, where the player has to guess a word one letter at a time.<br> 
    If the player guesses a letter that is in the word, it will be revealed. If the player guesses a letter that is not in the word,<br>
    they lose a life. The player has 6 lives in total.<br>

 * The hangman_logo function displayed in blue, using the Colorama library. The play_hangman function is the main 
 game loop and is responsible for managing the state of the game and updating the player's progress. The setup_game function sets up the
 game by selecting a random word from a list and setting the number of lives allowed, the words variable is defined in words,py file
 provided.<br>
<br>
<br>
<br>
<br>
 ![amiresposive](assets/hangman%20home%20page.jpg)

# Design
## The design of a hangman game includes a few key elements:
  * A word or phrase to be guessed: This is the main focus of the game, displayed underscores, with each space representing a letter in the word or phrase.
  * A "hangman" image: This image is gradually drawn as players make incorrect guesses, with the final image being a complete picture of a person being "hanged."
  * A message or counter: This displays the number of incorrect guesses remaining or message if player wins or lost.
  * A list of correctly guessed letters: This keeps track of the letters that have been correctly guessed and displays them to the player.
  * A list of incorrectly guessed letters: This keeps track of the letters that have been incorrectly guessed and displays them to the player.
  
![amiresposive](images/hangman%20home%20page.png)




# Features and user experience 
<br>
<br>
<br>
<br>

## Features 
<br>
<br>
* The features in this specific hangman game include:
  *  An ASCII art representation of the hangman game that is displayed as the player progresses through the game
  *  A limited number of lives (6) to guess the word
  *  The game uses words that have been imported from a separate file "words.py"
  *  The game checks if the user entered valid name with only Alphabets
  *  The game also displays the letters that have been used
  *  The game uses 'colorama' library to change the color of the text, making the game more visually appealing
  *  The game uses a loop to allow the user to keep playing the game until they win or lose.
  *  It also uses a function 'play_game()' but it's not implemented in the main part of the game.
  *  The game randomly selects a word from a list of words, and displays it to the user as a series of underscores (one for each letter in the word), with correctly guessed letters filled in.

## user experience 

<br>
<br>
* In this specific hangman game, the user's goal is to guess the correct word by guessing letters one at a time. 
* The user will have a certain number of lives (in this case, 6), and for each incorrect letter guessed, they will lose one life.
* The user must guess the correct word before running out of lives in order to win the game.
* The user's ultimate goal is to correctly guess the hidden word before the stick figure of the hanging man is fully drawn. 



 
 
 
 
 
 
 
 ![amiresposive](assets/hangman-hangman%20flow%20chart.jpg)

# Features and user experience 
 * 
# Technologies Used
* Languages
* Python.
* Libraries
* random to select a random word.  word.py

# credited 
* Code Institute for the mock terminal for the deploy to a live site.
* How to add sleep for python from https://realpython.com/python-sleep/
* words.py - A list of randomly generated from free word - https://www.randomlists.com/data/words.json 
* Notepad ++ Column editor 
* For Templates free lucidchart https://lucid.app/
* Word Document with python https://youtu.be/WK-0VQsEfLA 
  https://lucid.app/lucidchart/7af783b3-f411-40d5-9e8a-e2e60a4977a6/edit?invitationId=inv_84c2610d-ede7-44d3-8c53-350bb3ca8d4f

<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>


<br>
<br>
<br>














###  Why I called hangman for all is my Son is under 10 years I approach him to play so that he can practice his spelling, Vocabulary, and letters. Since we are not native English speakers it helps for general knowledge








![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Suzan Dewitz,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!