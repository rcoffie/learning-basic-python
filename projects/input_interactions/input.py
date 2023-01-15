
def get_age():
    ''' age variable set to an empty string '''
    age = ""
    while age.isdigit() == False:
        age = input("how old are you ? ")
        if age.isdigit() == False:
            print('please enter is a digit number for the age')
        
    return f"you are  {age} years old "


age = get_age()
print(age)