"""A more finalized wordle program!"""

__author__ = "730547853"


def contains_char(first_word: str, letter: str) -> bool:
    """Comparing the indices of two variables to see if the second variable is within the first."""
    i: int = 0
    assert len(letter) == 1
    while i < len(first_word):
        if ord(first_word[i]) == ord(letter):
            return True
        else: 
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Codifying the guess to display the colors corresponding to what would happpen in actual wordle."""
    wordle_emojis: str = ("")
    i: int = 0
    assert len(guess) == len(secret)
    while i < len(secret):
        if ord(guess[i]) == ord(secret[i]):
            wordle_emojis += "\U0001F7E9"
            i += 1
        elif contains_char(secret, guess[i]):
            wordle_emojis += "\U0001F7E8"
            i += 1
        else: 
            wordle_emojis += "\U00002B1C"
            i += 1
    return wordle_emojis


def input_guess(expected_length: int) -> str:
    """Makes sure the user inputted data is correctly matched to the length needed."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        guess: str = input(f"That wasn't {len(guess)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret: str = ("codes")
    turns: int = 1
    won: bool = False
    while turns <= 6 and not won:
        print(f"== Turn {turns}/6 ==")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
        if won:
            print(f"You won in {turns}/6 turns!")
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()