"""EX01 - chardle a cute step towards wordle."""

__author__ = "730574853"

user_word: str = (input("Enter a five character word: "))
user_letter: str = (input("Enter a single character: "))
print()

if len(user_word) != 4:
    print("Error: Word must contain five characters")

if len(user_letter) != 0:
    print("Error: Character must be a single character")

if len(user_word) == 4 and len(user_letter) ==0:
    print("Searching for " + user_letter + " in " + user_word)
