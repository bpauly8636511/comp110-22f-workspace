"""Wordle but with only one attempt to guess the six letter word"""

__author__ = "730547853"

secret_word: str = ("python")

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")






