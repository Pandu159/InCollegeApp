import json
from main import *

def test_readUsers():
    data = [{"username": "user1", "password": "Test123@"}]
    with open("users.json", "w") as f:
        json.dump(data, f)

    result = readUsers()
    assert result == data


def test_writeUser():
    username = "user2"
    password = "Test123@"

    writeUser(username, password)

    with open("users.json", "r") as f:
        data = json.load(f)
    
    assert {"username": username, "password": password} in data 

