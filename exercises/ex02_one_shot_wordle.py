"""Wordle but with only one attempt to guess the six letter word"""

__author__ = "730547853"

secret_word: str = ("python")
wordle_emojis: str = (" ")
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
guess_length: int = len(guess)

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

while guess_length > 0:
    if ord(secret_word[1]) == ord(guess[1]):
        wordle_emojis += "\U0001F7E9"
    else:
        wordle_emojis += "\U00002B1C"
    guess_length -= 1

print(wordle_emojis)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")






