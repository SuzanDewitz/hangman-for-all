# HANGMAN-For-ALL
  * HANGMAN for aLL is a Python terminal game, which runs on the Code Institute mock terminal on Heroku.The play_game function prints out some introductory messages
 to the user and describes the rules of the game. The game is played by guessing letters in a secret word, one at a time. If a letter 
 is in the word, it is revealed, but if the letter is not in the word, the player loses a life. The player has six lives to guess the 
 word before the game is over.
 * Hangman is a great game for spelling and vocabulary knowledge to recognize how letters fit together.The hangman game is a word guessing game that is typically used to teach or reinforce spelling and vocabulary skills. In the game, players are presented with a word or phrase and must guess the letters that make up that word or phrase before a "hangman" is fully drawn.
 <br>
 <br>

![hangman ami responsive](https://user-images.githubusercontent.com/114075332/212318531-b18fbf67-d524-4174-afd6-0764647c04dd.jpg)


 <br>
 <br>
 <br>
 <br>
 <br>

# Table of Contents
### Home
### How to play
### Future Features 
### User experience 
### User Goals
### Design 
### Flow chart  
### Tecnologies used
### Fixed and unfixed bugs
### Validation
### Testing
### Deployment
### Credits
 <br>
 <br>
 <br>

# Home
## How to play
  * This is a Python script that implements a simple game of Hangman, where the player has to guess a word one letter at a time.<br> 
    If the player guesses a letter that is in the word, it will be revealed. If the player guesses a letter that is not in the word,<br>
    they lose a life. The player has 6 lives in total.<br>

 * The hangman_logo function displayed in white, using the Colorama library. The play_hangman function is the main 
 game loop and is responsible for managing the state of the game and updating the player's progress. The setup_game function sets up the
 game by selecting a random word from a list and setting the number of lives allowed, the words variable is defined in words.py file
 provided.<br>
<br>
<br> 

![hangman home](https://user-images.githubusercontent.com/114075332/212319437-ab3a081c-1f6a-4728-a6a5-3b60ffadc342.jpg)

<br>
<br>


# Design
## The design of a hangman game includes a few key elements:
  * A word or phrase to be guessed: This is the main focus of the game, displayed underscores, with each space representing a letter in the word or phrase.
  * A "hangman" image: This image is gradually drawn as players make incorrect guesses, with the final image being a complete picture of a person being "hanged."
  * A message or counter: This displays the number of incorrect guesses remaining or message if player wins or lost.
  * A list of correctly guessed letters: This keeps track of the letters that have been correctly guessed and displays them to the player.
  * A list of incorrectly guessed letters: This keeps track of the letters that have been incorrectly guessed and displays them to the player.
<br>
<br>
<br>
<br>

# Future Features and user experience 
<br>
<br>
<br>
<br>

## Existing Features 
<br>


  *  The features in this specific hangman game include:
  *  An ASCII art representation of the hangman game that is displayed as the player progresses through the game
  *  A limited number of lives (6) to guess the word
  *  The game uses words that have been imported from a separate file "words.py"
  *  The game checks if the user entered valid name with only Alphabets
  *  The game also displays the letters that have been used
  *  The game uses 'colorama' library to change the color of the text, making the game more visually appealing
  *  The game uses a loop to allow the user to keep playing the game until they win or lose.
  *  It also uses a function 'play_game()' but it's not implemented in the main part of the game.
  *  The game randomly selects a word from a list of words, and displays it to the user as a series of underscores (one for each letter in the word), with correctly guessed letters filled in.
<br>
<br>
<br>
<br>

![hangman name rules](https://user-images.githubusercontent.com/114075332/212320036-cd67bf07-1a15-4ffe-bb08-fbcaa6ba01fa.jpg)


<br>
<br>

![hangman lives](https://user-images.githubusercontent.com/114075332/212326958-86f55c66-5da8-4a2d-828d-56e261182d20.jpg)

* A random word is selected from a separate file "words.py".

<br>
<br>

![hangman lives progress](https://user-images.githubusercontent.com/114075332/212326982-2105f56c-745b-479b-af21-f94cd948735e.jpg)

 *  The game checks if the user entered valid name with only Alphabets
 *  If the letter is in the word, it is revealed to the user and they are prompted to guess another letter.
<br>
<br>

![hangman won](https://user-images.githubusercontent.com/114075332/212325399-c61401bc-1d89-460d-9035-b73398c786b9.jpg)

* If the user correctly guesses all the letters in the word, they win the game and a message is displayed.
<br>
<br>

![hangman play no](https://user-images.githubusercontent.com/114075332/212325470-415e94f2-c845-432e-b361-5578516fef66.jpg)

*  The user can choose to play again or end the game. They can only write "n" or "y" If the user enter the word "n" the game will end.
<br>
<br>

![hangman guess lost](https://user-images.githubusercontent.com/114075332/212325507-5b3a5693-f2f4-4e76-b0c0-7cfc17c28ca7.jpg)

*   The user continues to guess letters until they have correctly guessed all the letters in the word or they run out of lives.
*   If the letter is not in the word, the user loses a life and an ASCII art image of the hangman is displayed to show the progress of the game.

<br>
<br>


![hangman play again](https://user-images.githubusercontent.com/114075332/212326215-7a7bee4a-75ba-4cbd-b26f-62dda11ca500.jpg)

*  The user can choose to play again or end the game."n" or "y" If user enter the letter  "y" the game will start.
*  In this script, the user is prompted to enter the letters in uppercase.<br> The script then converts all the letters in the word and used letters<br> to uppercase using the .upper() method.<br> The script compares the user input letter with the uppercase version of the letters<br> in the word. This ensures that the user can enter the letter <br>in either uppercase or lowercase, and the <br>script will be able to correctly compare it to the letters in the word.<br>This way, the user can play the game without worrying about the letter case.


<br>
<br>



# Future Features

* Adding a save game feature, so that players can save their progress and come back to the game later.
* Adding a timer to the game, where players have a certain amount of time to guess the word before the game ends.
* Adding a multiplayer mode, where players can play against each other online.
* Adding a difficulty increase feature, where the game gets harder as the player progress through the levels.
* Allowing players to select the difficulty level of the game, with different levels having different word lists and different numbers of allowed lives.

## user experience 

<br>
<br>

* The user experience of this hangman game script would involve the user being prompted to enter their name,then being given the rules of the game.  <br>The user would then be presented with a randomly selected word that they have to guess one letter at a time. If the letter is in the word, <br> it will be revealed, if not, the user loses a life. The user has 6 lives in total. The script also uses ASCII art to show the progress of the hangman game. <br>Overall, the user experience is interactive and visually engaging,<br> as the script uses colors and images to enhance the gameplay experience.<br>
<br>
<br>

# User Goals 
<br>
<br> 

* The user would also want to have fun and enjoy the interactive game play experience. 
* The user can improve their vocabulary or spelling skills by playing the game.
* The main goal for the user in this hangman game script would be to correctly guess the randomly selected word before running out of lives. 

<br>
<br>
<br>
<br>

# Flow chart  

* using flowcharts it is very useful tool for understanding the structure and logic of a script, particularly for a complex or long code like this hangman game script.
 A flowchart can help to clearly visualize the different steps involved in the game and how they are connected, making it easier to understand the overall logic of the script and identify any potential issues or areas for improvement.
<br>
<br>

 ![hangman flow chart](https://user-images.githubusercontent.com/114075332/212324626-39dce7fe-5bff-46e5-a702-7610b486f19b.jpg)


<br>
<br>
<br>
<br>
 
# Technologies Used
<br>
<br>
<br>


#### Libraries Used
*  Git - For version control These commands were used for version control during project:

+   git add . - To add files before committing
+   git commit -m "write your text to mentioning changes" - To commit changes to the local repository
+   git push - To push all committed changes to the GitHub repository
 #### for README
+   git add README.md
+   git commit -m "docs: add README.md file"
+   git push - To push all committed changes to the GitHub repository
<br>
<br>

### Languages Used 
<br>

+  This tool is created purely using Python language.
* This script is written in Python, which is a popular language used for creating games.
* The script uses the "random" library to randomly select a word from a list of words. 
* The script imports the "words" variable from the word.py file which contains the list of words. 
* The script also uses the "time" library to insert delay between certain actions, like between showing the rules of the game.
* The script uses the "colorama" library to add color to the game's logo and ASCII art images.
*  The script also uses the "random" library to randomly select a word from a list of words. 
* The script defines several functions, including "hangman_logo()" which displays the game's logo, "play_game()" which welcomes the player to the game and explains the rules, and "play_hangman 
    (word, lives_allowed)" which is the main game loop.
* In the main loop, the script keeps track of the letters that have been used, and if the user correctly guesses all the letters of the word, they win the game. If the user runs out of lives, they 
   lose the game.
* It also uses the ASCII art images to display the progress of the game to the user which makes it more interactive.
It also uses the input function to take inputs from the user and validate it.

<br>
<br>
<br>
<br>

## Fixed and unfixed bugs
### Fixed Bugs 

<br>
<br>

*  Python Linter Test
   * The Bugs "E501 line too long" 
    + This error occurs when i try to add "HANGMAN-FOR-AL" The line of code was too long and goes beyond the recommended limit of 79 characters thats why i change to "HNAGMAN"
    + There where more line to long 
    + I fix the error, I split the long line into multiple shorter lines by:
      * I Moved some of the code to the next line
      * I used parentheses and backslashes to indicate line continuation
      *  I used explicit line continuation with a backslash
   *  "W291 trailing whitespace"
   *  "W605 invalid escope sequence'\ ' "
    + I used autopep8 tool it help me to automatically format the code to conform to the PEP8 style guide.
    + To use autopep8 to fix "W291 trailing whitespace" error, I used following command:
      1.  pip install pep8
      2.  autopep8 --in-place --aggressive --aggressive run.py





![hangman image erorr](https://user-images.githubusercontent.com/114075332/212372493-91255b4b-a812-4531-be0e-c3476540739a.jpg)

<br>
<br>

* The Bugs "E501 line too long" 
    + This error occurs when i try to add "HANGMAN-FOR-AL" The line of code was too long and goes beyond the recommended limit of 79 characters thats why i change to "HNAGMAN"

![hangman-tolong erorr](https://user-images.githubusercontent.com/114075332/212372967-eec115d6-ca41-44c6-bc15-e68f966c9be7.jpg)

<br>
<br>

## unfixed bugs
* There no unfixed bugs




<br>
<br>
<br>
<br>


## Validation
### Python Linter Test 
* Test result: No errors found. 
* Since pep8 no longer working ,From slack team i have been told to validated Code Institute Python linter. Test result: No errors found. It showed no warnings or problems as in screenshot below.
<br>
<br>

![hangman no erorr](https://user-images.githubusercontent.com/114075332/212372549-72b4be34-03bb-4283-af2b-dac1b0968d09.jpg)

<br>
<br>
<br>
<br>

## Deployment
#### Project Deployment on Heroku
*    From the Heroku dashboard I clicked the create new app button, named the app and selected the Europe region and clicked 'Create app'
*    Choose connect to GitHub account 
*    Search for the repository you want to deploy. The name needs to match exactly in my case"Hangman-For-All" 
*    Click 'Connect' 
*    When the deployment is complete, go to the 'Settings' page to configure vars and buildpacks.
*    Click 'Add' to fill out PORT and 8000 in he KEY / VALUE pair. This has been done.
*    Scroll down to 'Buildpacks'. Click the 'Add Buildpack' button.
*    From the pop up window, select 'python' and save changes.
*    Repeat this again for'node.js' and save the changes. It is 'important' to make sure the buildpacks are in the correct order
    The ordering is as follows:

    1. `heroku/python`
    2. `heroku/nodejs` with 'Python' first and 'node.js' second.<br> If they are not in the correct order, drag them into the right order.
     
   
* The app is then built, and we get an app was successfully built message and a button to take me to the deployed link.
* After the settings are done, navigate to the 'Deploy' tab at the top left side.
* Select the option 'Github, 'connect to github' as the deployment method.
* Search for the Github Repository in the search field (Hangman-For-All) and start 'Search'.
* When the search is complete the link to github repository will appear, click 'connect'.
* Once the repository is connected to Heroku
* I used manually deploy by selecting a branch to deploy from and clicking 'Deploy Branch'.
* Manual deployment allows the update the app whenever 'Deploy Branch' is clicked.
* Once the build process completes take a few seconds, live app could be viewed by clicking button "View" below 'Your app was successfully deployed'.
+  Link generated: https://hangman-for-all.herokuapp.com/





# credited 
* Code Institute for the mock terminal for the deploy to a live site.
* How to add sleep for python from https://realpython.com/python-sleep/
* words.py - A list of randomly generated from free word - https://www.randomlists.com/data/words.json 
* Notepad ++ Column editor 
* For Templates free lucidchart https://lucid.app/
* Word Document with python https://youtu.be/WK-0VQsEfLA 
* https://lucid.app/lucidchart/7af783b3-f411-40d5-9e8a-e2e60a4977a6/edit?invitationId=inv_84c2610d-ede7-44d3-8c53-350bb3ca8d4f

<br>

<br>
<br>
<br>



####  Why I called hangman for all is my Son is under 10 years I approach him to play Hangman so that he can practice his spelling, Vocabulary, and letters. Since we are not native English speakers it helps for general knowledge too for any one at any age "learning by playing!"








