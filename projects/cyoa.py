"""This program is a make your own adventure where you must take care of a friend cat until it loves you!"""

__author__ = "730574853"

POINTS: int = 0
PLAYER: str = ""

def main() -> None:
    greet()


def greet() -> None:
    """A welcome message that also gets the users name."""
    #please add welcome message
    global PLAYER_NAME 
    PLAYER += input(str("What is your name? "))

if __name__ == "__main__":
    main()