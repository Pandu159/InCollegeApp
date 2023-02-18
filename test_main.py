import json
import pytest
from main import *
from authentication import *
from feed import *
import io
import sys
from unittest.mock import patch

def test_homeScreen(capsys):
    HomeScreen()
    out, err = capsys.readouterr()
    message = "Welcome to InCollege!\n"
    message += "Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.\n"
    message += "After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.\n"
    message += "He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.\n"
    assert message == out

def test_signIn(capsys, monkeypatch):
    users = [{"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith"}]
    with open("users.json", "w") as f:
        json.dump(users, f)

    def mock_input(prompt):
        if "username" in prompt:
            return "user1"
        else:
            return "Test123@"

    monkeypatch.setattr("builtins.input", mock_input)

    fullName = signIn()
    out, err = capsys.readouterr()

    assert fullName == "Tom Smith"
    assert "Successfully logged in!" in out


def test_signUp(capsys, monkeypatch):
    users = [{"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith"}]
    with open("users.json", "w") as f:
        json.dump(users, f)

    test_inputs = ['user2', 'Test123#', 'John', 'Doe']
    monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))

    signUp()
    out, err = capsys.readouterr()
    assert "Successfully signed up!" in out

    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": "user2", "password": "Test123#", "firstName": "John", "lastName": "Doe"} in data

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
                         [([1], "under construction\n"),
                          ([2], "under construction\n"),
                          ([3], "under construction\n"),
                          ([4], "under construction\n"),
                          ([5], "under construction\n"),
                          ([6], ""),
                          ([7], "Not a valid option\n")])
def test_selectSkill(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        selectSkill()
    except SystemExit:
        out, err = capsys.readouterr()
        assert messages in out

@pytest.mark.parametrize("test_inputs, test_inputs1, messages",
                         [(['Engineer', 'Good job', 'USF', 'Tampa', '100'], ['Dentist', 'Great job', 'FIU', 'Miami', '200'],
                           "Job created! Returning back to options...\n")])
def test_createJob(capsys, monkeypatch, test_inputs, test_inputs1, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createJob('Tom Smith')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        createJob('John Doe')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

        
def test_getJobs():
    data = [{"title": "Engineer", "description": "Good job", "employer": "USF", "location": "Tampa", "salary": "100", "Name": "Tom Smith"},
           {"title": "Dentist", "description": "Great job", "employer": "FIU", "location": "Miami", "salary": "200", "Name": "John Doe"} ]
    with open("jobs.json", "w") as f:
        json.dump(data, f)

    result = getJobs()
    assert result == data


def test_printJobs(capsys):
    printJobs()
    out, err = capsys.readouterr()

    message = 'Job: 1\n\n'
    message += 'Title: Engineer\n'
    message += 'Description: Good job\n'
    message += 'Employer: USF\n'
    message += 'Location: Tampa\n'
    message += 'Salary: 100\n\n\n'
    message += 'Job: 2\n\n'
    message += 'Title: Dentist\n'
    message += 'Description: Great job\n'
    message += 'Employer: FIU\n'
    message += 'Location: Miami\n'
    message += 'Salary: 200\n\n\n'
    assert message == out     


@pytest.mark.parametrize("test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4, messages",
                         [(['Y', 'Engineer', 'Good job', 'USF', 'Tampa', '100'], ['Y','Dentist', 'Great job', 'FIU', 'Miami', '200'],
                         ['Y', 'Jornalist', 'Great job', 'FIU', 'Miami', '100'], ['Y','Nurse', 'Good job', 'FIU', 'Miami', '200'],
                         ['Y', 'Physician', 'Great job', 'USF', 'Tampa', '200'], "Job created! Returning back to options...\n")])
def test_findJob(capsys, monkeypatch, test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        findJob('Tom Smith')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        findJob('John Doe')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs2.pop(0))
        findJob('John Doe')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs3.pop(0))
        findJob('John Doe')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out   

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs4.pop(0))
        findJob('Tom Smith')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    findJob('Tom Smith')
    out, err = capsys.readouterr()
    assert "Job list is full! Returning to options..." in out
    
   

@pytest.mark.parametrize("test_inputs, test_inputs1, messages, messages1",
                         [(['Tom', 'Smith'],['Jim', 'Frey'],
                           "They are a part of the InCollege system\n", "They are not yet a part of the InCollege system")])
def test_findPeople(capsys, monkeypatch, test_inputs, test_inputs1, messages, messages1) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        findPeople()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        findPeople()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages1 in out
