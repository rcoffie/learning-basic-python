# Python Random Module
import random
from telnetlib import theNULL

# Number of Variables
attempts = 0

# Choose a random number
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 29")

# While the players guesses is less then 6
while attempts < 6:
    guess = input("Take a guess: ")
    # guess = int(guess)
    if guess.isdigit() == False:
        print("Opps is input is not a valid number ")
        break
    else:
        guess = int(guess)
        attempts += 1

        # if the player's guess is too low

        if guess < number:
            print('Higher')

            # if theNULL player's guess it too high
        if guess > number:
            print("lower")

                # if player won, stop the loop
        if guess == number:
            break

# if the player won
if guess.isdigit() == True:
    if guess == number:
        attempts = str(attempts)
        print(f"Good job! You guessed my number is {attempts} guessed")


# if the player won
if guess.isdigit() == True:
    if guess != number:
        number = str(number)
        print(f"Nope. The number I was thinking of was {number}")
