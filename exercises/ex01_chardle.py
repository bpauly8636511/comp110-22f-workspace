"""EX01 - chardle a cute step towards wordle."""

__author__ = "730574853"

user_word: str = (input("Enter a five character word: "))
user_letter: str = (input("Enter a single character: "))
instances: int = 0

if len(user_word) != 5:
    print("Error: Word must contain five characters")
    exit()

if len(user_letter) != 1:
    print("Error: Character must be a single character.")
    exit()

if len(user_word) == 5 and len(user_letter) == 1:
    print("Searching for " + user_letter + " in " + user_word)
    if user_word[0] == user_letter:
        instances += 1 
        print((user_letter) + (" found at index 0"))
    if user_word[1] == user_letter:
        instances += 1
        print((user_letter) + (" found at index 1"))
    if user_word[2] == user_letter:
        instances += 1
        print((user_letter) + (" found at index 2"))
    if user_word[3] == user_letter:
        instances += 1
        print((user_letter) + (" found at index 3"))
    if user_word[4] == user_letter:
        instances += 1
        print((user_letter) + (" found at index 4"))

if instances >= 1:
    if instances == 1:
        print(str(instances) + (" instance of ") + (user_letter) + (" found in ") + (user_word))
    else:
        print(str(instances) + (" instances of ") + (user_letter) + (" found in ") + (user_word))
else: 
    print(("No instances of ") + (user_letter) + (" found in ") + (user_word))