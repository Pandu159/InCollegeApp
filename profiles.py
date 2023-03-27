from network_utils import *
from helper import *
from job_utils import *
from authentication import *
import json


def readProfiles():
    try:
        with open("profiles.json", "r") as f:
            file_contents = f.read()
            if file_contents:
                return json.loads(file_contents)
            else:
                return []
    except FileNotFoundError:
        return []


def writeProfile(username, title, major, university, about, experience, education):
    data = readProfiles()
    major = formatInput(major)
    university = formatInput(university)
    data = [i for i in data if i["username"] != username]
    data.append({"username": username, "title": title, "major": major, "university": university,
                 "about": about, "experience": experience, "education": education})
    with open("profiles.json", "w") as f:
        json.dump(data, f)


def updateProfile(username, updateParam, updateInfo):
    profiles = readProfiles()

    for i, profile in enumerate(profiles):
        if username == profile["username"]:
            profiles[i][updateParam] = updateInfo
            with open("profiles.json", "w") as f:
                json.dump(profiles, f)


def createProfile(username):
    existingProfile = readProfiles()
    existingProfile = [i for i in existingProfile if i['username'] == username]
    existingProfile = existingProfile[0] if existingProfile else None
    if existingProfile:
        modifyProfile(username, existingProfile)
        return

    print("Starting to create profile\n")
    title = input("Please enter a title for your profile: ")
    major = input("Please enter your major: ")
    university = input("Please enter the name of your university: ")
    about = input("Please enter a paragraph about yourself: ")
    experience = []
    education = []
    count = 0
    while count < 3:
        addExperience = input("Do you want to add experience (yes/no)?: ")
        if addExperience.lower() == "yes":
            count = +1
            exp = {}
            exp["title"] = input("Please enter the title of the job: ")
            exp["employer"] = input("Please enter the employer: ")
            exp["date started"] = input("Please enter the date started (MM/DD/YYYY): ")
            exp["date ended"] = input("Please enter the date ended (MM/DD/YYYY): ")
            exp["location"] = input("Please enter the location: ")
            exp["description"] = input("Please enter a description of what you did: ")
            experience.append(exp)
        else:
            break
    while True:
        addEducation = input("Do you want to add education (yes/no)?: ")
        if addEducation.lower() == "yes":
            edu = {}
            edu["school name"] = input("Please enter the name of the school: ")
            edu["degree"] = input("Please enter your degree: ")
            edu["years attended"] = input("Please enter the years attended (YYYY-YYYY): ")
            education.append(edu)
        else:
            break
    writeProfile(username, title, major, university, about, experience, education)
    updateUserInfo(username, "profile", "profile")
    print("Profile created successfully!")
    printProfile(username)
    selection = int(input("Input 0 to return to previous screen.\n"))
    returnToOption(selection, username)


def modifyProfile(username, existingProfile):
    print("Starting to modify profile\n")
    title = input("Please enter a title for your profile (or press enter to keep current value): ")
    major = input("Please enter your major (or press enter to keep current value): ")
    university = input("Please enter the name of your university (or press enter to keep current value): ")
    about = input("Please enter a paragraph about yourself (or press enter to keep current value): ")
    experience = []
    education = []

    count = 0
    while count < 3:
        addExperience = input("Do you want to add/modify experience (yes/no)?: ")
        if addExperience.lower() == "yes":
            exp = {}
            exp["title"] = input("Please enter the title of the job: ")
            exp["employer"] = input("Please enter the employer: ")
            exp["date started"] = input("Please enter the date started (MM/DD/YYYY): ")
            exp["date ended"] = input("Please enter the date ended (MM/DD/YYYY): ")
            exp["location"] = input("Please enter the location: ")
            exp["description"] = input("Please enter a description of what you did: ")
            experience.append(exp)
        else:
            break
    while True:
        addEducation = input("Do you want to add/modify education (yes/no)?: ")
        if addEducation.lower() == "yes":
            edu = {}
            edu["school name"] = input("Please enter the name of the school: ")
            edu["degree"] = input("Please enter your degree: ")
            edu["years attended"] = input("Please enter the years attended (YYYY-YYYY): ")
            education.append(edu)
        else:
            break

    if title:
        updateProfile(username, "title", title)
    else:
        title = existingProfile["title"]

    if major:
        updateProfile(username, "major", major)
    else:
        major = existingProfile["major"]

    if university:
        updateProfile(username, "university", university)
    else:
        university = existingProfile["university"]

    if about:
        updateProfile(username, "about", about)
    else:
        about = existingProfile["about"]

    if experience:
        updateProfile(username, "experience", experience)
    else:
        experience = existingProfile["experience"]

    if education:
        updateProfile(username, "education", education)
    else:
        education = existingProfile["education"]

    writeProfile(username, title, major, university, about, experience, education)
    print("Profile updated successfully!")
    printProfile(username)
    selection = int(input("Input 0 to return to previous screen.\n"))
    returnToOption(selection, username)


def formatInput(string):
    words = string.split()
    formatted = [word.capitalize() for word in words]
    return " ".join(formatted)


def viewMyProfile(username):
    users = readUsers()
    for user in users:
        if user["username"] == username:
            if user["profile"] is None:
                print("You have not created your profile yet.")
                selection = int(input("Input 0 to return to previous screen or 1 to Create your profile: "))
                if selection == 0:
                    returnToOption(selection, username)
                else:
                    createProfile(username)
            else:
                printProfile(username)

            selection1 = int(input("Input 0 to return to previous screen.\n"))
            returnToOption(selection1, username)


def printProfile(username):
    users = readUsers()
    for user in users:
        if user["username"] == username:
            name = user["firstName"] + " " + user["lastName"]
            print("\n" + name)

    profiles = readProfiles()
    for profile in profiles:
        if profile["username"] == username:
            print("Title: " + profile["title"])
            print("Major: " + profile["major"])
            print("University: " + profile["university"])
            print("About: " + profile["about"])

            if len(profile["experience"]) != 0:
                print("Experience: \n")
                for experience in profile["experience"]:
                    print("Title: " + experience["title"])
                    print("Employer: " + experience["employer"])
                    print("Date started: " + experience["date started"])
                    print("Date ended: " + experience["date ended"])
                    print("Location: " + experience["location"])
                    print("Description: " + experience["description"] + "\n")

            if len(profile["education"]) == 0:
                print("Education: no education added yet to profile.")
            else:
                print("Education: \n")
                for education in profile["education"]:
                    print("School Name: " + education["school name"])
                    print("Degree: " + education["degree"])
                    print("Years attended: " + education["years attended"])


def friendsProfile(username):
    users = readUsers()

    for user in users:
        if user["username"] == username:
            if len(user["friends"]) != 0:
                friendsList = []
                print("List of friends: ")

                for friend in user["friends"]:
                    users1 = readUsers()

                    listLine = {}
                    for userFriends in users1:
                        if userFriends["username"] == friend:
                            listLine["username"] = friend
                            listLine["firstName"] = userFriends["firstName"]
                            listLine["lastName"] = userFriends["lastName"]
                            listLine["profile"] = userFriends["profile"]
                            friendsList.append(listLine)
                            break

                profile = False
                for friends in friendsList:
                    if friends["profile"] is None:
                        displayedName = "Username: " + friends["username"] + " - Name: " + friends["firstName"] + " " + \
                                        friends["lastName"]
                    else:
                        displayedName = "Username: " + friends["username"] + " - Name: " + friends["firstName"] + " " + \
                                        friends["lastName"] + " (Profile)"
                        profile = True
                    print(displayedName)

                if profile == False:
                    print("None of your friends have created a profile yet")
                    break
                else:
                    userName = input("Please enter the username of a friend to view profile: ")
                    invalidUser = True
                    for friends in friendsList:
                        if friends["username"] == userName:
                            invalidUser = False
                            if friends["profile"] is not None:
                                printProfile(userName)
                                break
                            else:
                                print("No profile available")
                                break
                    if invalidUser == True:
                        print("Invalid username.")

            else:
                print("You do not have any friend yet.")

    selection = int(input("Input 0 to return to previous screen.\n"))
    returnToOption(selection, username)


# this function checks whether the current user is friends with the target user
def checkFriend(username, targetUser):
    # gets a list of users from users.json
    users = getJson("users")

    # searches user list for current user
    for user in users:
        if user["username"] == username:
            # if friends list is not empty:
            if len(user["friends"]) != 0:
                # seraches friends list for target user
                for friend in user["friends"]:
                    # target user is found, returns true
                    if friend == targetUser:
                        return True
                # target user was not found, returns false
                return False
            # friends list is empty, returns false
            else:
                return False


# this function sends a message to the target user from the current user
def sendMessage(username, targetUser):
    # check if current user is friends with target user or if the user is a Plus member
    if checkFriend(username, targetUser) or checkAccountTier(username) == "Plus" or checkAccountTier(targetUser) == "Plus":
        # initialize bool flag for valid user inbox
        flag = False

        # gets message from input
        message = input("What is your message: ")

        # gets the list of inboxes
        inboxes = getJson("inbox")

        # search for target user's inbox
        for inbox in inboxes:
            if inbox["username"] == targetUser:
                # check if inbox is a dictionary or a list
                if isinstance(inbox["inbox"], list):
                    newMessage = [{"senderUsername": username, "message": message}]
                    newMessage.extend(inbox["inbox"])
                    inbox["inbox"] = newMessage
                elif isinstance(inbox["inbox"], dict):
                    inbox["inbox"] = {"senderUsername": username, "message": message}
                flag = True
                break
        # target user's inbox has not been created
        if not flag:
            createInbox(username)
            sendMessage(username, targetUser)  # this will not be called infinitely bc flag will become true

        # appends message in target user's inbox with a return username
        try:
            with open("inbox.json", "w") as f:
                json.dump(inboxes, f)
        except FileNotFoundError:
            print("inbox.json missing!")
            return
    # if current user is not friends with target user, it prints an error
    else:
        print("I'm sorry, you are not friends with that person.")


# this function checks the inbox of the current user and prints messages, if any
def checkInbox(username):
    # opens inbox.json as a list of inboxes
    inboxes = getJson("inbox")

    # search through inbox for current user's inbox
    for inbox in inboxes:
        # current user's inbox is found
        if inbox["username"] == username:
            # if inbox is not empty
            if len(inbox["inbox"]) != 0:
                # print message
                for entry in inbox["inbox"]:
                    message = entry["message"]
                    sender = entry["senderUsername"]
                    print(f"Message:  {message}")
                    print(f"From: {sender}")

                    # asks user if they would like to respond or delete this message, it is otherwise left in inbox
                    response1 = input("Would you like to respond to this message? (yes/no)")
                    if response1.lower() == "yes":
                        # respond to that message using the sender's username
                        sendMessage(username, entry["senderUsername"])
                    response2 = input("Would you like to delete this message? (yes/no)")
                    if response2.lower() == "yes":
                        # removes message from the inbox
                        inbox["inbox"].remove(entry)

                        # opens inbox.json to update the inbox
                        try:
                            with open("inbox.json", "w") as f:
                                json.dump(inboxes, f)
                        except FileNotFoundError:
                            print("inbox.json missing!")
                            return
            # inbox is empty
            else:
                print("Inbox is empty")
        # current user's inbox is not found
        else:
            print(username, "'s inbox is not found")


# this function checks if the current user has any messages at startup
def checkMessageStart(username):
    # opens list of users as users
    inboxes = getJson("inbox")

    # search through users for username
    for userInbox in inboxes:
        # user's inbox is found
        if userInbox["username"] == username:
            # messages are found
            if len(userInbox["inbox"]) != 0:
                return True
            # no messages are found
            else:
                return False
        # user's inbox is not found
        else:
            return False


# this function creates an empty inbox for the current user
def createInbox(username):
    # create empty inbox
    newInbox = {}
    newInbox["username"] = username
    newInbox["inbox"] = []

    # open list of inboxes to insert empty inbox
    inboxes = getJson("inbox")
    inboxes.append(newInbox)

    # dump inboxes back into json
    try:
        with open("inbox.json", "w") as f:
            json.dump(inboxes, f)
    except:
        print("inbox.json missing!")
        return


def checkAccountTier(username):
    users = getJson("users")

    for user in users:
        if user["username"] == username:
            return user["accountTier"]
