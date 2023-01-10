# HANGMAN-For-ALL
  *HANGMAN for aLL is a Python terminal game, which runs on the Code Institute mock terminal on Heroku.The play_game function prints out some introductory messages
 to the user and describes the rules of the game. The game is played by guessing letters in a secret word, one at a time. If a letter 
 is in the word, it is revealed, but if the letter is not in the word, the player loses a life. The player has six lives to guess the 
 word before the game is over.
 * Hangman is a great game for spelling and vocabulary knowledge to recognize how letters fit together to form English words as well as know how to spell words so that the user can guess the correct letters.wide range of vocabulary in order to correctly guess the mystery words.
 <br>
 <br>
 <br>

  ![amiresposive](assets/hangman%20ami%20responsive.jpg)

* Home
 * How to play
 * Design
 * Features and user experience 
 
 * Tecnologies used
 * Fixed and unfixed bugs
 * Validation
 * Testing
 * Project creation and deployment
 * Credits
 <br>
 <br>
 <br>

 How to play




Hangman-For-All
# Home
* about Hangman-For-All
  * The hangman_logo function seems to display the hangman logo in blue, using the colorama library. The play_hangman function is the main 
game loop, and is responsible for managing the state of the game and updating the player's progress. The setup_game function sets up the
 game by selecting a random word from a list and setting the number of lives allowed, the words variable is defined in words,py file
 provided.



# Design
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