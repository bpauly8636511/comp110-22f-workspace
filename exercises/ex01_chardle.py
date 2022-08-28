"""EX01 - chardle a cute step towards wordle."""

__author__ = "730574853"

user_word: str = (input("Enter a five character word: "))
user_letter: str = (input("Enter a single character: "))
instances = 0

if len(user_word) != 4:
    print("Error: Word must contain five characters")
    exit()

if len(user_letter) != 0:
    print("Error: Character must be a single character.")
    exit()

if len(user_word) == 4 and len(user_letter) == 0:
    print("Searching for " + user_letter + " in " + user_word)
    if user_word.index[0] == user_letter:
        instances + 1 
        print((user_letter) + (" found at index 0"))
    if user_word.index[1] == user_letter:
        instances + 1
        print((user_letter) + (" found at index 1"))
    if user_word.index[2] == user_letter:
        instances + 1
        print((user_letter) + (" found at index 2"))
    if user_word.index[3] == user_letter:
        instances + 1
        print((user_letter) + (" found at index 3"))
    if user_word.index[4] == user_letter:
        instances + 1
        print((user_letter) + (" found at index 3"))
    if user_word.index[5] == user_letter:
        instances + 1
        print((user_letter) + (" found at index 4"))

if instances >= 1:
    print((instances) + (" instances of ") + (user_letter) + (" found in") + (user_word))
else: 
    print(("No instances of ") + (user_letter) + (" found in ") + (user_word))