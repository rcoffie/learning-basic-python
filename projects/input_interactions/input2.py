
def play_again():

    answer = ''

    while answer.lower() not in ['y','n']:
        answer = input('do you want to play again?: ')

        if answer.lower() == 'y':
            return True 
        elif  answer.lower() == 'n' :
            return False 
        else:
            print('Enter Y or N only ')

play_again = play_again()

print(play_again)