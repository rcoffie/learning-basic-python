import json

# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"we 'll remember you when you come back , {username}!")


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("what is your name? ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back , {username}! ")


    else:
        print(f"Welcome back, {username}! ")

greet_user()
