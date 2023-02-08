import json
from main import *

def test_readUsers():
    data = [{"username": "user1", "password": "Test123@"}]
    with open("users.json", "w") as f:
        json.dump(data, f)

    result = readUsers()
    assert result == data

def test_writeUser():
    username = "user1"
    password = "Test123@"

    writeUser(username, password)

    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": username, "password": password} in data

def test_checkPassword():
    goodPassword = ["testTest1!", "Testtwo12@"]
    for p in goodPassword:
        assert checkPassword(p) == True

    badPassword = ["test7", "badpassword1"]
    for p in badPassword:
        assert checkPassword(p) == False

def test_findJob():
    pass

def test_findPeople():
    pass

def test_main():
    test_signUp()
    test_signIn()

def test_signUp():
    username = "user1"
    password = "Test123@"
    result = readUsers()
    if len(result) > 5:
        assert "All permitted accounts have been created, please come back later."
    else:
        writeUser(username, password)
        assert "Successfully Signed up"

def test_signIn():
    username = "user1"
    password = "Test123@"
    if signIn():
        assert "Successfully Signed up"
    else:
        assert "User information invalid. Please enter again."
        assert test_selectOption()

def test_selectOption():
    option = [1,2,3]
    if option == 1:
        test_findJob()
    elif option == 2:
        test_findPeople()
    elif option == 3:
        test_selectSkill()

def test_selectSkill():
    skill = [1,2,3, 4, 5, 6]
    if skill == 0:
        print("under construction")
    elif skill == 2:
        print("under construction")
    elif skill == 3:
        print("under construction")
    elif skill == 4:
        print("under construction")
    elif skill == 5:
        print("under construction")
    elif skill == 6:
        test_selectOption()

#test_main()