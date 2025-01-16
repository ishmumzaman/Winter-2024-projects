from random import *

listword = ["huntsman", "enrichment", "significance","lightyear","kawasaki"]
randomword = choice(listword)
listrandom = list(randomword)




def hyphen(randomword):
    hyp = []
    for i in randomword:
        hyp.append("-")
    return hyp
x= hyphen(randomword)
print(f"Hello, Welcome to Hangman. Your word is {x}, you have 8 tries left, good luck")

def confirm_letter():
    while (True):
        guess = input("Input a letter: ")
        if guess.isalpha() == True and (len(guess) == 1):

            return guess
        else:
            print("Please enter only a letter")

life = 8
while life > 0 and listrandom != x:
    guess1 = confirm_letter()

    if guess1 in listrandom:
        print("Correct!")

        for index, letter in enumerate(listrandom):
            if letter == guess1:
                x[index] = guess1
    else:
        print("Incorrect!")
        life -= 1

    print(f"Lives left: {life}")
    print(f"Current word: {''.join(x)}")

if life == 0:
    print(f"Game over! The word was '{randomword}'. Better luck next time!")
else:
    print(f"Congratulations! You guessed the word '{randomword}'!")
























