"""This program is a make your own adventure where you must take care of a friend cat until it loves you!"""

__author__ = "730574853"


from random import randint
POINTS: int = 0
PLAYER: str = ""
NEKO: str = ""


def main() -> None:
    """What makes the rest of my program run."""
    global POINTS
    greet()
    adventure_one()
    POINTS = adventure_two(POINTS) + POINTS
    print(f"Congrats {PLAYER}! You have {POINTS} love points!")
    game_loop()
    print(f"Congrats {PLAYER}! You finished with {POINTS} love points!")


def greet() -> None:
    """A welcome message that also gets the users name."""
    #please add welcome message
    global PLAYER 
    PLAYER += input(str("What is your name? "))
    print("Welcome! Your goal is to make your Neko love you! You can do this by getting love points!")
    global NEKO
    user_input: int = int(input("Please choose Neko 1: \U0001F431 or Neko 2: \U0001F408 by entering 1 or 2: "))
    while (user_input != 1) and (user_input != 2):
        user_input = int(input("Please enter 1 or 2 for Neko 1 or Neko 2: "))
    if user_input == 1:
        NEKO = "\U0001F431"
    else: 
        NEKO = "\U0001F408"
    print(f"Congrats on your new Neko No Tomodachi! {NEKO} Take good care of them!")


def adventure_one() -> None:
    """The point of this procedure is to begin the adventure with your neko to make it grow closer to 100 points using globals."""
    global POINTS
    global PLAYER
    print(f"1. Pet your Neko! \U0001F63A {NEKO}")
    print(f"2. Feed your Neko! \U0001F638 {NEKO}")
    print(f"3. Play with your Neko! \U0001F63C {NEKO}")
    users_choice: int = int(input("Please choose a number 1 through 3 for one of the three options: "))
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please enter 1, 2 or 3: "))
    if users_choice == 1:
        POINTS += 20
        print(f"Congrats {PLAYER}! You have {POINTS} love points!")
    elif users_choice == 2:
        POINTS += 25
        print(f"Congrats {PLAYER}! You have {POINTS} love points!")
    elif users_choice == 3:
        POINTS += 15
        print(f"Congrats {PLAYER}! You have {POINTS} love points!")


def adventure_two(x: int) -> int:
    """The point of this function is to add random points to the global variable at the end because cats are random."""
    print(f"1. Give your Neko a belly rub!")
    print(f"2. Hug your Neko!")
    print(f"3. Give your Neko a kiss!")
    users_choice: int = int(input("Please choose option 1, 2, or three! "))
    global PLAYER
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please enter 1, 2, or 3! "))
    if users_choice == 1:
        x += randint(-10, 100)
        print(f"Sorry {PLAYER} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x
    elif users_choice == 2:
        x += randint(-10, 20)
        print(f"Sorry {PLAYER} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x
    elif users_choice == 3:
        x += randint(-10, 40)
        print(f"Sorry {PLAYER} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x


def game_loop() -> None:
    print(f"You may choose from three options, would you like to continue the game with route 1? ")
    print(f"Continue the game with route 2? ")
    print(f"Or end the game, Aka route 3?")
    users_choice: int = int(input("Please choose 1, 2, or 3 for route 1, route 2, or route 3: "))
    global POINTS
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please choose 1, 2, or 3!"))
    while users_choice != 3:
        if users_choice == 1:
            adventure_one()
            print(f"Congrats {PLAYER}! You have {POINTS} love points!")
        if users_choice == 2:
            POINTS = adventure_two(POINTS)
            print(f"Congrats {PLAYER}! You have {POINTS} love points!")
        users_choice: int = int(input("Please choose 1, 2, or 3 for route 1, route 2, or route 3: "))       


if __name__ == "__main__":
    main()