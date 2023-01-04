# # defining a function 

# def greet_user():
#     """ Display a simple greeting. """
#     print("hello")

# greet_user()

# # Passing Information to a Function 

# def greet_user(username):
#     print(f"hello, {username.title()}")

# greet_user('samson')

# def display_message():
#     print("Learning and understanding functions ")

# display_message()


# def favorite_book(book):
#     print(f"One of my favoirte book is {book.title()}")

# favorite_book('Alice and the Wonderland')

# Positional Arguments and keyowrd Aguement

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('Dog', 'Black')
# describe_pet(animal_type="Monkey", pet_name="Storm")
# describe_pet(pet_name="zimbo", animal_type="parrot")


# # Default Aguement
# def describe_pet(pet_name, animal_type="dog"):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(pet_name="doggie")
# describe_pet('donny', 'cat')


# Returnig values in functions

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name(first_name='samsson',last_name='wezzy')
# print(musician)

# # Optional Aguement 

# def get_formatted_name(first_name,  middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name

# footballer = get_formatted_name(first_name='Junior',middle_name='Bebeto',last_name='Do Santos')
# print(footballer)

# # Return dictonaries 

# def build_person(first_name, last_name,):
#     person = {'first':first_name, 'last':last_name}
#     return person 

# employer_1 = build_person('doku','benard')

# print(employer_1)

# def build_person(firstt_name,  last_name, middle_name=None):
#     person = {'first':firstt_name, 'last':last_name, 'middle':middle_name}
#     if middle_name:
#         person['middle'] = middle_name
#     return person

# employer_2 = build_person('John','Anderson')
# print(employer_2)


# passing list in functions 

# def greet_users(names):
#     '''Print a simple greetings to each user in the list'''
#     for name in names:
#         msg = f"hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah','ty','margot','simon','benard','joe']
# greet_users(usernames)



# Modifying a list in  a functon 
# def print_models(unprinted_designs, completed_models):

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe folloing models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron','gucci']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Passing an Attribute a number of aguements 

def make_pizza(*toppings):
    print("making pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('peperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# Mixing Positional and Arbitary Arguments

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

# Using Keyword aguements 

def build_profile(first, last, **user_info):
    user_info['first_name']= first 
    user_info['last_name'] = last 

    return user_info 

user_profile = build_profile(
    'albert','einstein',
    location='kumasi',
    field = 'physcis'
)

print(user_profile)