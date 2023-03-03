from network_utils import *
from helper import *
from job_utils import *
from authentication import *
from feed import *
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
            count =+1
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
    print("Profile created successfully!")


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

def formatInput(string):
    words = string.split()
    formatted = [word.capitalize() for word in words]
    return " ".join(formatted)