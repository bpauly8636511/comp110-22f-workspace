"""A more finalized wordle program!"""

__author__ = "730547853"

wordle_emojis: str = (" ")

"""Comparing the indices of two variables to see if the second variable is within the first."""
def contains_char(first_word: str, letter: str) -> bool:
    i: int = 0
    assert len(letter) == 1
    while i < len(first_word):
        if ord(first_word[i]) == ord(letter):
            return True
        else: 
            i += 1
    if i >= len(first_word) and not True:
        return False

"""Codifying the guess to display the colors corresponding to what would happpen in actual wordle."""
def emojified(guess: str, secret: str) -> str:
    i: int = 0
    assert len(guess) == len(secret)
    while i < len(secret):
        if ord(guess[i]) == ord(secret[i]):
            wordle_emojis += "\U0001F7E9"
            i += 1
        elif contains_char:
            wordle_emojis += "\U0001F7E8"
            i += 1
        else: 
            wordle_emojis += "\U00002B1C"
            i += 1

def input_guess(expected_length: int) -> int:
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        guess: str = input(f"That wasn't {len(guess)} chars! Try again: ")
    if len(guess) == expected_length:
        return guess

"""The entrypoint of the program and the main game loop."""
def main() -> None:
    secret: str = ("codes")
    turns: int = 0
    won: bool = False
    while turns <= 6 and not won:
        print(f"== Turn {turns}/6 ==")
        input_guess(5)
        emojified(guess, secret)
        print(emojified)
        if ord(guess) == ord(secret):
            won = True
        else:
            turns += 1

if __name__ == "__main__":
    main()

    
    



