import os

import pytest
from feed import *
from network_utils import *
from unittest.mock import patch, MagicMock, mock_open
from tempfile import NamedTemporaryFile
import json


def test_homeScreen(capsys):
    homeScreen()
    out, err = capsys.readouterr()
    message = "Welcome to InCollege!\n"
    message += "Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.\n"
    message += "After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.\n"
    message += "He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.\n"
    assert message == out


@pytest.mark.parametrize("test_inputs, messages",
                         [([4], ""),
                          ([6], "Invalid Selection!\n")])
def test_mainPage(capsys, monkeypatch, test_inputs, messages) -> None:
    messages1 = "Input 9 to view a video that would explain why joining InCollege would be highly beneficial for you\n"
    messages1 += "Input 2 to explore Useful Links or Input 3 to explore InCollege Important Links\n"

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        mainPage()
    except SystemExit:
        out, err = capsys.readouterr()
        messages1 += messages
        assert messages1 in out


@patch("builtins.input")
def test_signIn(input_mock):
    input_mock.side_effect = ["username", "password"]
    readUsers_mock = MagicMock(return_value=[{"username": "username", "password": "password", "language": "en"}])
    with patch("authentication.readUsers", readUsers_mock):
        result = signIn()
        assert result == "username"


@patch("builtins.input")
@patch("authentication.readUsers")
@patch("authentication.writeUser")
def test_signUp(writeUser_mock, readUsers_mock, input_mock):
    input_mock.side_effect = ["new_username", "Test123!", "First", "Last", "College", "Major"]
    readUsers_mock.return_value = [{"username": "existing_username", "password": "password", "language": "en"}]
    result = signUp()
    writeUser_mock.assert_called_with("new_username", "Test123!", "First", "Last", "College", "Major", "English",
                                      "on", "on", "on", [], [], None)
    assert result == "new_username"


@patch("builtins.open", new_callable=mock_open,
       read_data='[{"username": "user1", "password": "password1", "language": "en"}]')
def test_readUsers(open_mock):
    result = readUsers()
    open_mock.assert_called_with("users.json", "r")
    assert result == [{"username": "user1", "password": "password1", "language": "en"}]


def test_checkPassword():
    goodPassword = ["testTest1!", "Testtwo12@"]
    for p in goodPassword:
        assert checkPassword(p) == True

    badPassword = ["test7", "badpassword1"]
    for p in badPassword:
        assert checkPassword(p) == False


def test_getJson(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_data.json"
    # Write some sample data to the file
    with open(test_file, "w") as f:
        json.dump(
            {"title": "Engineer", "description": "Good job", "employer": "USF", "location": "Tampa", "salary": 100.0,
             "Name": "Tom Smith"}, f)

    # Call the function to load the data
    data = getJson(str(tmp_path / "test_data"))
    assert data == {"title": "Engineer", "description": "Good job", "employer": "USF", "location": "Tampa",
                    "salary": 100.0, "Name": "Tom Smith"}


@pytest.mark.parametrize("test_inputs, test_inputs1, messages",
                         [(['Engineer', 'Good job', 'USF', 'Tampa', '100'],
                           ['Dentist', 'Great job', 'FIU', 'Miami', '200'],
                           "Job created! Returning back to options...\n")])
def test_createJob(capsys, monkeypatch, test_inputs, test_inputs1, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createJob("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        createJob("user2")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out


@pytest.mark.parametrize("test_input, message",
                         [(['Test Job', 'Test Description', 'Test School', 'Test City', '100'],
                           "Job created! Returning back to options...\n")])
def test_createJob(capsys, monkeypatch, test_input, message) -> None:
    # Get the original contents of the jobs.json file
    with open("jobs.json", "r") as f:
        data = json.load(f)
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input.pop(0))
        createJob("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert message in out

    # Rewrite the original file with the old contents
    with open("jobs.json", "w") as f:
        json.dump(data, f)


def test_writeUser():
    # Get the original contents of the jobs.json file
    with open("users.json", "r") as f:
        data = json.load(f)

    username = "user1"
    password = "Test123@"
    firstName = "Tom"
    lastName = "Smith"
    language = "English"
    inCollegeEmail = "on"
    SMS = "on"
    targetedAds = "on"
    college = "USF"
    major = "Computer Science"
    friends = ""
    friendRequests = ""
    profile = ""
    writeUser(username, password, firstName, lastName, college, major, language, inCollegeEmail, SMS, targetedAds,
              friends, friendRequests, profile)

    with open("users.json", "r") as f:
        usersData = json.load(f)

    assert {"username": username, "password": password, "firstName": firstName, "lastName": lastName,
            "language": language, "inCollegeEmail": inCollegeEmail, "SMS": SMS, "targetedAds": targetedAds,
            "college": college, "major": major, "friends": friends, "friendRequests": friendRequests,
            "profile": profile} in usersData

    # Rewrite the original file with the old contents
    with open("users.json", "w") as f:
        json.dump(data, f)


@pytest.mark.parametrize("test_input, message",
                         [(['Test Job', 'Test Description', 'Test School', 'Test City', '100'],
                           "Job created! Returning back to options...\n")])
def test_printJobs(capsys, monkeypatch, test_input, message) -> None:
    # Get the original contents of the jobs.json file
    with open("jobs.json", "r") as f:
        data = json.load(f)

    message = 'Job: 1\n\n'
    message += 'Title: Engineer\n'
    message += 'Description: Good job\n'
    message += 'Employer: USF\n'
    message += 'Location: Tampa\n'
    message += 'Salary: 100.0\n\n\n'

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input.pop(0))
        createJob("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert message.strip() == '\n'.join(out.strip().split('\n')[:7])

    # Rewrite the original file with the old contents
    with open("jobs.json", "w") as f:
        json.dump(data, f)


@pytest.mark.parametrize("test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4, messages",
                         [(['Y', 'Engineer', 'Good job', 'USF', 'Tampa', '100'],
                           ['Y', 'Dentist', 'Great job', 'FIU', 'Miami', '200'],
                           ['Y', 'Jornalist', 'Great job', 'FIU', 'Miami', '100'],
                           ['Y', 'Nurse', 'Good job', 'FIU', 'Miami', '200'],
                           ['Y', 'Physician', 'Great job', 'USF', 'Tampa', '200'],
                           "Job created! Returning back to options...\n")])
def test_findJob(capsys, monkeypatch, test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4,
                 messages) -> None:
    # Get the original contents of the jobs.json file
    with open("jobs.json", "r") as f:
        data = json.load(f)

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        findJob('user1')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        findJob('user2')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs2.pop(0))
        findJob('user2')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs3.pop(0))
        findJob('user2')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs4.pop(0))
        findJob('user1')
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    findJob('user1')
    out, err = capsys.readouterr()
    assert "Job list is full! Returning to options..." in out

    # Rewrite the original file with the old contents
    with open("jobs.json", "w") as f:
        json.dump(data, f)


@pytest.mark.parametrize("test_input1, test_input2, message1, message2",
                         [(['Tom', 'Smith'], ['Jim', 'Frey'],
                           "They are a part of the InCollege system\n",
                           "They are not yet a part of the InCollege system")])
def test_findPeople(capsys, monkeypatch, test_input1, test_input2, message1, message2) -> None:
    # Get the original contents of the jobs.json file
    with open("users.json", "r") as f:
        data = json.load(f)

    with open("users.json", "w") as f:
        json.dump([{"firstName": "Tom", "lastName": "Smith"}], f)

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input1.pop(0))
        findPeople()
    except IndexError:
        out, err = capsys.readouterr()
        assert message1 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input2.pop(0))
        findPeople()
    except IndexError:
        out, err = capsys.readouterr()
        assert message2 in out

    # Rewrite the original file with the old contents
    with open("users.json", "w") as f:
        json.dump(data, f)



@pytest.mark.parametrize("test_inputs, test_inputs1, messages, messages1",
                         [(['1', '0', '2', '0', '3', '0'], ['4', '0', '5', '0'],
                           "under construction\nunder construction\nunder construction",
                           "under construction\nunder construction\n")])
def test_selectSkill(capsys, monkeypatch, test_inputs, test_inputs1, messages, messages1) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        selectSkill("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs1.pop(0))
        selectSkill("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages1 in out


@pytest.mark.parametrize("test_inputs, messages",
                         [(['1', '2', '3', '9', '12'],
                           "InCollege Email successfully turned off, returning to previous menu...\nSMS successfully "
                           "turned off, returning to previous menu...\nTargeted Advertising successfully turned off, "
                           "returning to previous menu...\nReturning to previous menu...\nInvalid option, "
                           "returning to previous menu...\n")])
def test_guestControls(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        guestControls("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out


@pytest.mark.parametrize("test_input1, test_input2, test_message1, test_message2",
                         [(['2', '3', '4'], ['1', '2'],
                           "under construction\nunder construction\nunder construction\n",
                           "We're here to help\n",
                           )])
def test_selectUsefulLinks(monkeypatch, capsys, test_input1, test_message1, test_input2, test_message2):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input1.pop(0))
        selectUsefulLinks(1, "user1")
    except IndexError or KeyError:
        out, err = capsys.readouterr()
        assert test_message1 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input2.pop(0))
        selectUsefulLinks(1, "user1")
    except IndexError or KeyError:
        out, err = capsys.readouterr()
        assert test_message2 in out


@pytest.mark.parametrize("test_input1, test_input2, test_input3, test_input4, test_input5, test_message1, "
                         "test_message2, test_message3, test_message4, test_message5",
                         [(['1', '0'], ['2', '0'], ['3', '0', '4', '0'], ['5', 'N', '0'], ['6', '0'],
                           # test message 1
                           "Copyright © 2023 InCollege. All rights reserved.\nAll materials on this website, "
                           "including but not limited to text, graphics, logos, images, and software, "
                           "are the property of InCollege and are protected by copyright laws. InCollege prohibits "
                           "any reproduction, modification, distribution, transmission, or display of any content on "
                           "this website without prior written permission.\n\nBy using this website, you acknowledge "
                           "that you have read and understood this copyright notice and agree to abide by its terms "
                           "and conditions.\n",
                           # test message 2
                           "About\nIntroducing InCollege, a platform designed specifically for college students to "
                           "connect and grow their professional networks.\nYou are about to embark on an exciting "
                           "journey filled with opportunities and challenges. By connecting you with other "
                           "like-minded individuals, mentors, and employers, we are here to support you every step of "
                           "the way.\n",
                           # test message 3
                           "Accessibility options\nUser Agreement = yes\nThis User Agreement regulates your use of "
                           "the Company's website and is a legal agreement between you and InCollege. You agree to be "
                           "bound by this Agreement by accessing or using the Website. \n"
                           "Use of the Website. The Company provides you a non-exclusive, non-transferable, revocable "
                           "license to access and use the Website solely for personal, non-commercial purposes. You "
                           "agree not to use the Website for any illegal purpose or in any way that could harm, "
                           "disable, overburden, or impair it.\n",
                           # test message 4
                           "Welcome user0!\n\nPrivacy Policy:\nInCollege is committed to protecting your personal "
                           "information. This Privacy Policy outlines how we collect, handle, and share personal "
                           "information collected from you while using our website InCollege.\n"
                           "We Gather Data. We may collect personal information, such as your name, email address, "
                           "and phone number, as well as non-personal information, such as your IP address and "
                           "browsing history, when you visit our Website.\n",
                           # test message 5
                           "Cookie Policy:\nOn our website, InCollege uses cookies and similar technologies to give a "
                           "better user experience and to better understand how users use our website. This Cookie "
                           "Policy defines cookies and how we utilize them.\n"
                           "What exactly are cookies? When you visit a website, little text files called cookies are "
                           "placed on your device. Cookies enable a website to identify your device and save "
                           "information about your preferences or previous actions. Cookies are divided into two "
                           "types: session cookies, which are temporary and expire when you close your browser, "
                           "and persistent cookies, which remain on your device until they expire or are erased.\n"
                           "How We Make Use of Cookies. We use cookies to enhance your experience on our site and to "
                           "better understand how users interact with it.\n"
                           )])
def test_selectInCollegeImportant(capsys, monkeypatch, test_input1, test_message1, test_input2, test_message2,
                                  test_input3, test_message3, test_input4, test_message4, test_input5, test_message5):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input1.pop(0))
        selectInCollegeImportant(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message1 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input2.pop(0))
        selectInCollegeImportant(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message2 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input3.pop(0))
        selectInCollegeImportant(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message3 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input4.pop(0))
        selectInCollegeImportant(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message4 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input5.pop(0))
        selectInCollegeImportant(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message5 in out




@pytest.mark.parametrize("test_input1, test_input2, test_message1, test_message2",
                         [(['2', '0', '3', '0', '4', '0'], ['5', '0', '6', '0', '7', '0'],
                           "We're here to help\nIn College: Welcome to In College, the world's largest college "
                           "student network with many users in many countries and territories worldwide.\n"
                           "In College Pressroom: Stay on top of the latest news, updates, and reports\n",
                           "Under construction\nUnder construction\nUnder construction\n")])
def test_selectGeneral(capsys, monkeypatch, test_input1, test_input2, test_message1, test_message2):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input1.pop(0))
        selectGeneral(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message1 in out

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input2.pop(0))
        selectGeneral(0, "user0")
    except IndexError:
        out, err = capsys.readouterr()
        assert test_message2 in out


@pytest.mark.parametrize("test_input1, test_message1",
                         [(['3', '1'],
                           "under construction\n")])
def test_selectOption(capsys, monkeypatch, test_input1, test_message1):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input1.pop(0))
        selectOption("user1")
    except IndexError or KeyError:
        out, err = capsys.readouterr()
        assert test_message1 in out


@pytest.mark.parametrize("test_message", ['You have pending friend requests\n'])
def test_requestDisplay(capsys, monkeypatch, test_message):
    # Get the original contents of the jobs.json file
    with open("users.json", "r") as f:
        data = json.load(f)

    writeUser("test_user", "password", "Test", "User", "USF", "CS", "test", "mail@test.come", "off", "off", ["Test"],
              ["Test"], "")
    requestDisplay("test_user")

    try:
        requestDisplay("test_user")
    except TypeError:
        out, err = capsys.readouterr()
        assert test_message in out

    # Rewrite the original file with the old contents
    with open("users.json", "w") as f:
        json.dump(data, f)


@pytest.mark.parametrize("test_message", ['You have pending friend requests:\nFriendRequest'])
def test_checkFriendRequests(capsys, monkeypatch, test_message):
    # Get the original contents of the jobs.json file
    with open("users.json", "r") as f:
        data = json.load(f)

    writeUser("test_user_check_friend_requests", "password", "Test", "User", "USF", "CS", "test", "mail@test.come",
              "off", "off", ["Test"],
              ["FriendRequest"], "")
    try:
        checkFriendRequests("test_user_check_friend_requests")
    except OSError:
        out, err = capsys.readouterr()
        assert test_message in out

    # Rewrite the original file with the old contents
    with open("users.json", "w") as f:
        json.dump(data, f)

def test_writeProfile():
    # Get the original contents of the profiles.json file
    with open("profiles.json", "r") as f:
        data = json.load(f)

    username = "u1"
    title = "InCollegeProfile"
    major = "Computer Science"
    university = "University Of South Florida"
    about = "this is the paragraph about myself"
    experience = [
        {"title": "student", "employer": "usf", "date started": "01/01/2023", "date ended": "", "location": "tampa,fl",
         "description": "attended classes"}]
    education = [{"school name": "usf", "degree": "bachelors", "years attended": "2023-2023"}]
    writeProfile(username, title, major, university, about, experience, education)

    with open("profiles.json", "r") as f:
        test_data = json.load(f)

    assert {"username": username, "title": title, "major": major, "university": university,
            "about": about, "experience": experience, "education": education} in test_data

    # Rewrite the original file with the old contents
    with open("profiles.json", "w") as f:
        json.dump(data, f)


@pytest.fixture(autouse=True)
def test_readProfiles():
    data = readProfiles()
    with open("profiles.json", "r") as f:
        profiles = json.load(f)

    assert data == profiles


@pytest.mark.parametrize(" test_message",
                         [("\nTest User\nTitle: InCollegeProfile\nMajor: Computer "
                           'Science"\n"University": "University Of South Florida"\n"About": "this is '
                           'the paragraph about myself"\nExperience: \n\n"Title": "student"\n"Employer": '
                           '"usf"\n"Date started": "01/01/2023"\n"date ended": ""\n"Location": "tampa,'
                           'fl"\n"Description": "attended classes"\n\n"Education"\n\n"School Name": '
                           '"usf"\n"Degree": "bachelors"\n"Years attended": "2023-2023"\n')])
def test_printProfile(capsys, monkeypatch, test_message):
    # Get the original contents of the profiles.json file
    with open("users.json", "r") as f:
        userData = json.load(f)

    with open("profiles.json", "r") as f:
        profilesData = json.load(f)

    with open("users.json", "w") as f:
        json.dump([{"username":"testuser","firstName": "Test", "lastName": "User"}], f)

    with open("profiles.json", "w") as f:
        json.dump([{"username": "testuser", "title": "InCollegeProfile", "major": "Computer Science", "university": "University Of South Florida", "about": "this is the paragraph about myself", "experience": [{"title": "student", "employer": "usf", "date started": "01/01/2023", "date ended": "", "location": "tampa,fl", "description": "attended classes"}], "education": [{"school name": "usf", "degree": "bachelors", "years attended": "2023-2023"}]}], f)

    try:
        printProfile("testuser")
    except OSError:
        out, err = capsys.readouterr()
        assert test_message in out

    # Rewrite the original file with the old contents
    with open("users.json", "w") as f:
        json.dump(userData, f)
    with open("profiles.json", "w") as f:
        json.dump(profilesData, f)


def test_updateProfile():
    with open("profiles.json", "r") as f:
        profilesData = json.load(f)

    # calls updateProfile with a valid parameter
    with open("profiles.json", "w") as f:
        json.dump([{"username": "testuser", "title": "InCollegeProfile", "major": "Computer Science", "university": "University Of South Florida", "about": "this is the paragraph about myself", "experience": [{"title": "student", "employer": "usf", "date started": "01/01/2023", "date ended": "", "location": "tampa,fl", "description": "attended classes"}], "education": [{"school name": "usf", "degree": "bachelors", "years attended": "2023-2023"}]}], f)

    updateProfile("testuser", "major", "Information Technology")

    # reads the test file and verifies that the profile was updated
    with open("profiles.json", "r") as f:
        updated_profiles = json.load(f)
        assert updated_profiles[0]["major"] == "Information Technology"

    with open("profiles.json", "w") as f:
        json.dump(profilesData, f)

@pytest.mark.parametrize("test_input, test_message",
                         [(["InCollegeProfile", "Computer Science", "University of South Florida",
                            "the paragraph about myself", "yes", "student", "usf", "01012022", " test", "tampa",
                            "attended classes", "yes", "usf", "bachelors", "2023-2023"],
                           "Starting to create profile\n\n")])
def test_createProfile(test_input, test_message, monkeypatch, capsys):
    with open("profiles.json", "r") as f:
        profilesData = json.load(f)

    try:
        # calls createProfile with the test input
        test_username = "user1"
        monkeypatch.setattr('builtins.input', lambda _: test_input.pop(0))
        createProfile(test_username)
    except IndexError or KeyError:
        out, err = capsys.readouterr()
        assert test_message in out

    with open("profiles.json", "w") as f:
        json.dump(profilesData, f)



