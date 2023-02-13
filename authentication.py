import json


def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def writeUser(username, password, firstName, lastName):
    data = readUsers()

    data.append({"username": username, "password": password, "firstName": firstName, "lastName": lastName})
    with open("users.json", "w") as f:
        json.dump(data, f)


def signUp():
    users = readUsers()
    if len(users) >= 5:
        print("All permitted accounts have been created, please come back later.\n")
        return False

    while True:
        username = input("Please input a username: ")

        for user in users:
            if username == user["username"]:
                print("Username must be unique! Choose a different username.")
                continue
        break

    while True:
        password = input("Please input a password: ")
        if checkPassword(password):
            break
        else:
            print("Password must have minimum 8, maximum 12 characters, at least one capital letter, one digit, "
                  "and one special character")

    firstName = input("Please input your first name: ")
    lastName = input("Please input your last name: ")

    writeUser(username, password, firstName, lastName)

    print("Successfully signed up!")
    return firstName + " " + lastName


def signIn():

    while True:
        username = input("Please input a username: ")
        password = input("Please input a password: ")
        users = readUsers()

        for user in users:
            if username == user["username"]:
                if password == user["password"]:
                    print("Successfully logged in!")
                    fullName = user["firstName"] + " " + user["lastName"]
                    return fullName
        print("User information invalid. Please enter again. ")


def checkPassword(password):
    if 8 <= len(password) <= 12:
        has_upper = False
        has_digit = False
        has_special = False
        for char in password:
            if char.isdigit():
                has_digit = True
            elif char.isupper():
                has_upper = True
        has_special = any(char in "!@#$%^&*()_+-=[]{}|;':,.<>/?" for char in password)
        if has_upper and has_digit and has_special:
            return True
    return False
