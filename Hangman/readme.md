# Hangman

This Hangman script is one of my earliest Python projects created to explore basic programming concepts and test my overall Python skills. It uses fundamental elements such as loops, conditional statements, list manipulations, and user input. The program selects a random word from a predefined list and then challenges the user to guess it one letter at a time.

## Core Ideas and Logic

The script begins by importing the random choice function. It maintains a list of possible words from which one is selected randomly. The chosen word is split into a list of characters so each position can be revealed when the correct letter is guessed. The game then prints a masked version of the word where each letter is replaced by a dash. This gives the user a visual clue regarding the length of the word.

When the game starts, the user is prompted to enter a letter. The program runs a validation function that ensures only a single alphabetical character is entered. If the letter is correct, all positions where that letter appears are revealed in the masked word. If the letter is incorrect, the user loses a life from a total of eight. The user continues guessing until they either lose all their lives or correctly guess every letter in the word.

## Key Functions and Structures

A function called `hyphen` creates the masked version of the word by replacing every character with a dash. This masked list is updated each time a correct guess is made.  
A function called `confirm_letter` ensures that the user is providing only a single alphabetical character. This helps avoid issues with incorrect inputs or empty entries.  
The main loop uses a `while` condition to keep running as long as the user still has lives remaining and the revealed letters do not yet match the chosen word. Each guess reduces a life if the letter is not in the word. A correct guess triggers a reveal of that letter in the mask.  
When lives reach zero, the game ends and reveals the correct word. If the user completes the word in time, it prints a congratulatory message.

## Possible Enhancements

You can add more words to the word list to increase variety.  
You can implement a difficulty level system by adjusting the number of lives or controlling the complexity of the words.  
You can provide hints or display previously guessed letters to assist the user.  
You can adapt the script to run in a graphical interface rather than the console for a more interactive feel.


