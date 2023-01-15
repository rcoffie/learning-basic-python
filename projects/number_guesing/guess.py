import random


guess = ''
num = 0
tries = 5
while guess != num and tries != 0 :
    guess = int(input('input and radom number between 0 and 100 '))
    num = random.randint(1,100)
    if guess == num:
        tries -= 1
        print('you won')
    elif guess > num:
        tries -= 1
        print('you guessed too high ')
    else:
        tries -= 1
        print('you guessed too low try a higher number')
