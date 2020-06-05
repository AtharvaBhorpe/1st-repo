import random
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice...")
    print (random.randint(1,6))

    roll_again = input("Roll the dice again?")