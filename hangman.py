# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 15:14:56 2026

@author: Revati Patil
"""

import random

words = ["cat", "dog", "book", "pen", "apple"]
word = random.choice(words)

guessed = []
display = ["_"] * len(word)
attempts = 6

print("Hangman Game")
print("Word:", " ".join(display))

while attempts > 0 and "_" in display:
    letter = input("Enter a letter: ")

    if letter in guessed:
        print("Already guessed")
        continue

    guessed.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print("Word:", " ".join(display))

if "_" not in display:
    print("You Win! Word is:", word)
else:
    print("Game Over! Word was:", word)