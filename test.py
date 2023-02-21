import pytest 
from feed import *


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


def test_signIn(capsys, monkeypatch):
    users = [
        {"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith", "language": "English",
         "inCollegeEmail": "on", "SMS": "on", "targetedAds": "on"}]
    with open("users.json", "w") as f:
        json.dump(users, f)

    def mock_input(prompt):
        if "username" in prompt:
            return "user1"
        else:
            return "Test123@"

    monkeypatch.setattr("builtins.input", mock_input)

    username = signIn()
    out, err = capsys.readouterr()

    assert username == "user1"
    assert "Successfully logged in!\n\nCurrent Language is English\n\n" in out


def test_signUp(capsys, monkeypatch):
    users = [
        {"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith", "language": "English",
         "inCollegeEmail": "on", "SMS": "on", "targetedAds": "on"}]
    with open("users.json", "w") as f:
        json.dump(users, f)

    test_inputs = ['user2', 'Test123#', 'John', 'Doe', 'English', 'on', 'on', 'on']
    monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))

    signUp()
    out, err = capsys.readouterr()
    assert "Successfully signed up!" in out

    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": "user2", "password": "Test123#", "firstName": "John", "lastName": "Doe", "language": "English",
            "inCollegeEmail": "on", "SMS": "on", "targetedAds": "on"} in data


@pytest.fixture(autouse=True)
def test_readUsers():
    data = [
        {"username": "user1", "password": "Test123@", "firstName": "Tom", "lastName": "Smith", "language": "English",
         "inCollegeEmail": "on", "SMS": "on", "targetedAds": "on"}]
    with open("users.json", "w") as f:
        json.dump(data, f)

    result = readUsers()
    assert result == data


def test_writeUser():
    username = "user1"
    password = "Test123@"
    firstName = "Tom"
    lastName = "Smith"
    language = "English"
    inCollegeEmail = "on"
    SMS = "on"
    targetedAds = "on"
    writeUser(username, password, firstName, lastName, language, inCollegeEmail, SMS, targetedAds)

    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": username, "password": password, "firstName": firstName, "lastName": lastName,
            "language": language, "inCollegeEmail": inCollegeEmail, "SMS": SMS, "targetedAds": targetedAds} in data

def test_updateUserInfo():
    username = "user1"
    password = "Test123@"
    firstName = "Tom"
    lastName = "Smith"
    language = "English"
    updateParam = "inCollegeEmail"
    updateInfo = "off"		
    SMS = "on"
    targetedAds = "on"
    updateUserInfo(username, updateParam, updateInfo)
    with open("users.json", "r") as f:
        data = json.load(f)

    assert {"username": username, "password": password, "firstName": firstName, "lastName": lastName,
            "language": language, "inCollegeEmail": "off", "SMS": SMS, "targetedAds": targetedAds} in data


def test_checkPassword():
    goodPassword = ["testTest1!", "Testtwo12@"]
    for p in goodPassword:
        assert checkPassword(p) == True

    badPassword = ["test7", "badpassword1"]
    for p in badPassword:
        assert checkPassword(p) == False


def test_getJson():
    data = [{"title": "Engineer", "description": "Good job", "employer": "USF", "location": "Tampa", "salary": "100",
             "Name": "Tom Smith"}]
    with open("test_jobs.json", "w") as f:
        json.dump(data, f)

    result = getJson("jobs")
    assert result[0] == data[0]


@pytest.mark.parametrize("test_inputs, test_inputs1, messages",
                         [(['Engineer', 'Good job', 'USF', 'Tampa', '100'], ['Dentist', 'Great job', 'FIU', 'Miami', '200'],
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



def test_printJobs(capsys):
    printJobs()
    out, err = capsys.readouterr()

    message = 'Job: 1\n\n'
    message += 'Title: Engineer\n'
    message += 'Description: Good job\n'
    message += 'Employer: USF\n'
    message += 'Location: Tampa\n'
    message += 'Salary: 100\n\n\n'
    assert message.strip() == '\n'.join(out.strip().split('\n')[:7])


@pytest.mark.parametrize("test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4, messages",
                         [(['Y','Engineer', 'Good job', 'USF', 'Tampa', '100'],['Y','Dentist', 'Great job', 'FIU', 'Miami', '200'], 
                         ['Y','Jornalist', 'Great job', 'FIU', 'Miami', '100'], ['Y','Nurse', 'Good job', 'FIU', 'Miami', '200'], 
                         ['Y','Physician', 'Great job', 'USF', 'Tampa', '200'], "Job created! Returning back to options...\n")])
def test_findJob(capsys, monkeypatch, test_inputs, test_inputs1, test_inputs2, test_inputs3, test_inputs4, messages) -> None:
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


@pytest.mark.parametrize("test_inputs, test_inputs1, messages, messages1",
                         [(['Tom', 'Smith'], ['Jim', 'Frey'],
                           "They are a part of the InCollege system\n",
                           "They are not yet a part of the InCollege system")])
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


@pytest.mark.parametrize("test_inputs, test_inputs1, messages, messages1",
                         [(['1', '0', '2', '0', '3', '0'], ['4', '0', '5', '0'],
                           "under construction\nunder construction\nunder construction\n", 
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
                           "InCollege Email successfully turned off, returning to previous menu...\nSMS successfully turned off, returning to previous menu...\nTargeted Advertising successfully turned off, returning to previous menu...\nReturning to previous menu...\nInvalid option, returning to previous menu...\n")])
def test_guestControls(capsys, monkeypatch, test_inputs, messages) -> None:
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        guestControls("user1")
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out


def test_selectUsefulLinks(monkeypatch, capsys):
    pass

def test_selectInCollegeImportant():
    pass

def test_selectGeneral():
    pass

def selectOption():
    pass
