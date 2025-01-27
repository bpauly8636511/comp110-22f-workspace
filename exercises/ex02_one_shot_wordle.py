"""Wordle but with only one attempt to guess the six letter word!"""

__author__ = "730547853"

secret_word: str = ("python")
wordle_emojis: str = (" ")
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
guess_length: int = 0

while len(guess) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! Try again: ")

while guess_length < len(guess):
    if ord(secret_word[guess_length]) == ord(guess[guess_length]):
        wordle_emojis += "\U0001F7E9"
        guess_length += 1
    else:
        yellow: bool = False
        guess_length_two: int = 0
        while yellow is not True and guess_length_two < len(secret_word):
            if ord(secret_word[guess_length_two]) == ord(guess[guess_length]):
                yellow = True
            else:
                guess_length_two += 1
        if yellow is False:
            wordle_emojis += "\U00002B1C"
            guess_length += 1
        elif yellow is True:
            wordle_emojis += "\U0001F7E8"
            guess_length += 1

print(wordle_emojis)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")