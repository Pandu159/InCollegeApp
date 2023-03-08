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

