"""This program is a make your own adventure where you must take care of a friend cat until it loves you!"""

__author__ = "730574853"


from random import randint
points: int = 0
player: str = ""
neko: str = ""


def main() -> None:
    """What makes the rest of my program run."""
    global points
    greet()
    adventure_one()
    points = adventure_two(points) + points
    print(f"Congrats {player}! You have {points} love points!")
    game_loop()
    print(f"Congrats {player}! You finished with {points} love points!")


def greet() -> None:
    """A welcome message that also gets the users name."""
    global player 
    player += input(str("What is your name? "))
    print("Welcome! Your goal is to make your Neko love you! You can do this by getting love points!")
    global neko
    user_input: int = int(input("Please choose Neko 1: \U0001F431 or Neko 2: \U0001F408 by entering 1 or 2: "))
    while (user_input != 1) and (user_input != 2):
        user_input = int(input("Please enter 1 or 2 for Neko 1 or Neko 2: "))
    if user_input == 1:
        neko = "\U0001F431"
    else: 
        neko = "\U0001F408"
    print(f"Congrats on your new Neko No Tomodachi! {neko} Take good care of them!")


def adventure_one() -> None:
    """The point of this procedure is to begin the adventure with your neko to make it grow closer to 100 points using globals."""
    global points
    global player
    global neko
    print(f"1. Pet your Neko! \U0001F63A {neko}")
    print(f"2. Feed your Neko! \U0001F638 {neko}")
    print(f"3. Play with your Neko! \U0001F63C {neko}")
    users_choice: int = int(input("Please choose a number 1 through 3 for one of the three options: "))
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please enter 1, 2 or 3: "))
    if users_choice == 1:
        points += 20
        print(f"Congrats {player}! You have {points} love points!")
    elif users_choice == 2:
        points += 25
        print(f"Congrats {player}! You have {points} love points!")
    elif users_choice == 3:
        points += 15
        print(f"Congrats {player}! You have {points} love points!")


def adventure_two(x: int) -> int:
    """The point of this function is to add random points to the global variable at the end because cats are random."""
    print("1. Give your Neko a belly rub!")
    print("2. Hug your Neko!")
    print("3. Give your Neko a kiss!")
    users_choice: int = int(input("Please choose option 1, 2, or three! "))
    global player
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please enter 1, 2, or 3! "))
    if users_choice == 1:
        x += randint(-10, 100)
        print(f"Sorry {player} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x
    elif users_choice == 2:
        x += randint(-10, 20)
        print(f"Sorry {player} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x
    elif users_choice == 3:
        x += randint(-10, 40)
        print(f"Sorry {player} Neko No Tomodachi can be a bit random... You've gained {x} love points!")
        return x


def game_loop() -> None:
    """This function loops in order for the user to run the game however many times they'd like."""
    print("You may choose from three options, would you like to continue the game with route 1? ")
    print("Continue the game with route 2? ")
    print("Or end the game, Aka route 3?")
    users_choice: int = int(input("Please choose 1, 2, or 3 for route 1, route 2, or route 3: "))
    global points
    while (users_choice != 1) and (users_choice != 2) and (users_choice != 3):
        users_choice = int(input("Incorrect input! Please choose 1, 2, or 3!"))
    while users_choice != 3:
        if users_choice == 1:
            adventure_one()
        if users_choice == 2:
            points = adventure_two(points)
            print(f"Congrats {player}! You have {points} love points!")
        users_choice: int = int(input("Please choose 1, 2, or 3 for route 1, route 2, or route 3: "))       


if __name__ == "__main__":
    main()