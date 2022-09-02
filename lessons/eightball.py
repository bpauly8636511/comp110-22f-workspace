"""eight ball lesson example week three"""

___author___ = "730548753"

from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0, 2)

if response == 0:
    print("Yes, def")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("yes ofc")
else:
    print("my sources say no")

