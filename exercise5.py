# snake water gun game using python 
import random

options = ["snake", "water", "gun"]

while True:
    computer = random.choice(options)
    user = input("choose in snake water and gun or 'q' to quit ").lower()
    if user == 'q':
        break
    if computer == user :
        print("it is a draw")
    elif (computer == "gun" and user == "snake") or (computer == "snake" and user == "water") or (computer == "water" and user == "gun"):
        print("computer wines")
    elif (computer == "snake" and user == "gun") or (computer == "water" and user == "snake") or (computer == "gun" and user == "water"):
        print("user wins")

