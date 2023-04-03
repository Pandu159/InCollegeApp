# authentication
import json
from profiles import *

from notifications import *


def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def writeUser(username, password, firstName, lastName, college, major, language, inCollegeEmail, SMS, targetedAds,
              friends, friendRequests, profile, jobsApplied, jobsSaved, accountTier, lastApplied):
    data = readUsers()

    data.append(
        {"username": username, "password": password, "firstName": firstName, "lastName": lastName, "college": college,
         "major": major, "language": language, "inCollegeEmail": inCollegeEmail, "SMS": SMS, "targetedAds": targetedAds,
         "friends": friends, "friendRequests": friendRequests, "profile": profile, "jobsApplied": jobsApplied, "jobsSaved": jobsSaved, "accountTier": accountTier, "notifications": [], "lastApplied": lastApplied, "newPosting": [], "newMessages": False})
    with open("users.json", "w") as f:
        json.dump(data, f)


def updateUserInfo(username, updateParam, updateInfo):
    users = readUsers()

    for user in users:
        if username == user["username"]:
            with open("users.json", "w") as f:
                user[updateParam] = updateInfo
                json.dump(users, f)


def signUp():
    users = readUsers()
    if len(users) >= 10:
        print("All permitted accounts have been created, please come back later.\n")
        return None

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
    college = input("Please input your College: ")
    major = input("Please input your major: ")

    # Epic 3 added default language as English
    # and inCollegeEmail, SMS, and targetedAds "on" as default
    language = "English"
    inCollegeEmail = "on"
    SMS = "on"
    targetedAds = "on"
    friends = []
    friendsRequest = []
    profile = None
    jobsApplied = []
    jobsSaved = []

    accountTier = "Standard"
    lastApplied = ""
    isAccountUpgraded = input("Would you like to upgrade your account to a plus membership for $10/month? (Y/n)")

    if isAccountUpgraded.lower() == 'y':
        accountTier = "Plus"

    writeUser(username, password, firstName, lastName, college, major, language, inCollegeEmail, SMS, targetedAds,
              friends, friendsRequest, profile, jobsApplied, jobsSaved, accountTier, lastApplied)

    # create empty inbox
    createInbox(username)

    print("Successfully signed up!")
    return username


def signIn():
    while True:
        username = input("Please input a username: ")
        password = input("Please input a password: ")
        users = readUsers()

        for user in users:
            if username == user["username"]:
                if password == user["password"]:
                    print("Successfully logged in!\n")
                    language = user["language"]
                    print(f"Current Language is {language} \n")

                    if lastApplied(username):
                        print("Remember – you're going to want to have a job when you graduate. Make sure that you "
                              "start to apply for jobs today!\n")

                    # checks user's inbox
                    #if checkMessageStart(username):
                        #print("You have messages in your inbox!\n")

                    hasProfile(username) #Checks profile
                    numJobsApplied(username) #Number of jobs applied
                    newJobPost(username) #Prints if there is a new job posting
                    hasMessages(username) #Prints if user has new messages

                    return username
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
