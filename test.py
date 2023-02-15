import json
import pytest
from main import *
from authentication import *
from feed import *

def test_homeScreen(capsys):
    HomeScreen()
    out, err = capsys.readouterr()
    message = "Welcome to InCollege!\n"
    message += "Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.\n"
    message += "After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.\n"
    message += "He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.\n"
    assert message == out

@pytest.fixture(autouse=True)
def test_readUsers():
    data = [{"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith"}]
    with open("users.json", "w") as f:
        json.dump(data, f)

    result = readUsers()
    assert result == data

def test_writeUser():
    username = "user1"
    password = "Test123@"
    firstName = "Tom"
    lastName= "Smith"
    writeUser(username, password, firstName, lastName)

    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": username, "password": password, "firstName": firstName, "lastName": lastName} in data

def test_checkPassword():
    goodPassword = ["testTest1!", "Testtwo12@"]
    for p in goodPassword:
        assert checkPassword(p) == True

    badPassword = ["test7", "badpassword1"]
    for p in badPassword:
        assert checkPassword(p) == False

@pytest.mark.parametrize("test_inputs, messages",
                         [(['Engineer', 'Good job', 'USF', 'Tampa', '100'],
                           "Job created! Returning back to options...\n")])
def test_createJob(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createJob('Tom Smith')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

@pytest.mark.parametrize("test_inputs, messages",
                         [(['Y'],
                           "Job created! Returning back to options...\n")])
def test_findJob(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        findJob('Tom Smith')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

@pytest.mark.parametrize("test_inputs, messages",
                         [(['Tom', 'Smith'],
                           "They are a part of the InCollege system\n")])
def test_findPeople(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        findPeople()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out
