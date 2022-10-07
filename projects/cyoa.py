"""This program is a make your own adventure where you must take care of a friend cat until it loves you!"""

__author__ = "730574853"

POINTS: int = 0
PLAYER: str = ""
NEKO: str = ("")

def main() -> None:
    greet()


def greet() -> None:
    """A welcome message that also gets the users name."""
    #please add welcome message
    global PLAYER_NAME 
    PLAYER += input(str("What is your name? "))
    global NEKO
    NEKO = input("Please choose Neko 1: " + /U000200D + "or Neko 2: " + /U0001F408 + "by entering 1 or 2")
    while NEKO != 1 or 2:
        NEKO = input("Please enter 1 or 2 for Neko 1 or Neko 2: ")
    if NEKO == 1:
        NEKO = /U000200D
    else: 
        NEKO = /U0001F408
    print(f"Congrats on your new Neko No Tomodachi! {NEKO} Take good care of them!")
    


if __name__ == "__main__":
    main()