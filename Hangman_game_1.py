#Hangman Game

import random

words=["Apple","Basket","Cap","Door","Elephant"]
word=random.choice(words)
attempt_guess=6
user_guess=[]
display=["_" for i in range(len(word))]

print("Hangman game starts now")
print("You have 6 incorrect attempts left")

while attempt_guess>0 and "_" in display:
    print(f"Word : {display}")
    guess=input("Enter a letter: ")

    if len(guess)!=1 or not guess.isalpha():
        print("Kindly,Enter a letter")

    if guess in user_guess:
        print("This letter is already guessed")
        continue

    user_guess.append(guess)

    if guess in word.lower():
        print("Correct guess!")
        for i in range(len(word)):
            if word[i].lower()== guess:
                display[i]= guess

    else:
        attempt_guess -= 1
        print(f"Incorrect guess!You have {attempt_guess} guesses left")

if "_" not in display:
    print("Congratulations!You found the word ",word)

else:
    print("Oops!Better luck next time")
    print("The word was ",word)
        
    
