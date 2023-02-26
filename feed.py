#feed 
from authentication import *


def mainPage():
    print("Input 9 to view a video that would explain why joining InCollege would be highly beneficial for you")
    print("Input 2 to explore Useful Links or Input 3 to explore InCollege Important Links")
    selection = int(input("To create an account, input 0, to sign in input 1: "))

    userName = None

    if selection == 0:
        userName = signUp()
    elif selection == 1:
        userName = signIn()
    elif selection == 9:
        print("Video is now playing!")
        mainPage()
    elif selection == 2:
        selectUsefulLinks(0, None)
    elif selection == 3:  # InCollegeImportant
        selectInCollegeImportant(0, None)

    else:
        print("Invalid Selection!")
        exit(-1)

    if userName is not None:
        selectOption(userName)


def homeScreen():
    print("Welcome to InCollege!")
    print("Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.")
    print("After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.")
    print("He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.")


def selectUsefulLinks(i, uName):

    link = int(input("Please select a skill to learn from the list:\n1-General\n2-Browse InCollege\n3-Business Solutions\n4-Directories\n5-Return to previous screen\n"))

    m = i

    if link == 1:
        selectGeneral(m, uName)
    elif link == 2:
        print("under construction")
        selectUsefulLinks(m, uName)
    elif link == 3:
        print("under construction")
        selectUsefulLinks(m, uName)
    elif link == 4:
        print("under construction")
        selectUsefulLinks(m, uName)
    elif link == 5:
        if(i == 0):
            mainPage()
        else:
            selectOption(uName)

    else:
        print("Not a valid option")
        exit(-1)


def selectInCollegeImportant(i, uName):

    link = int(input("Please select a link from the following:\n 1 - Copyright Notice\n 2 - About\n 3 - Accessibility\n 4 - User Agreement\n 5 - Privacy Policy\n "
                     "6 - Cookie Policy\n 7 - Brand Policy\n 8 - Languages\n 9 - Return to previous screen\n"))
    m=i
    # Copyright Notice
    if link == 1:
        print("Copyright Notice: Developers of InCollege App")
        print("Copyright © 2023 InCollege. All rights reserved.\nAll materials on this website, including but not limited to text, graphics, logos, images, and software, are the property of InCollege and are protected by copyright laws. InCollege prohibits any reproduction, modification, distribution, transmission, or display of any content on this website without prior written permission.\n")
        print("By using this website, you acknowledge that you have read and understood this copyright notice and agree to abide by its terms and conditions.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # About
    elif link == 2:
        print("About\nIntroducing InCollege, a platform designed specifically for college students to connect and grow their professional networks.\nYou are about to embark on an exciting journey filled with opportunities and challenges. By connecting you with other like-minded individuals, mentors, and employers, we are here to support you every step of the way.\n")
        print("Our platform is designed to help you build your professional network, showcase your skills and experiences, and discover exciting career opportunities whether you're just starting your academic career or nearing graduation.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # Accessibility
    elif link == 3:
        print("Accessibility options")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # User Agreement
    elif link == 4:
        print("User Agreement = yes")
        print("This User Agreement regulates your use of the Company's website and is a legal agreement between you and InCollege. You agree to be bound by this Agreement by accessing or using the Website. ")
        print("Use of the Website. The Company provides you a non-exclusive, non-transferable, revocable license to access and use the Website solely for personal, non-commercial purposes. You agree not to use the Website for any illegal purpose or in any way that could harm, disable, overburden, or impair it.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # Privacy Policy
    elif link == 5:
        # A signed-in user will have the option to edit their Guest Controls
        if uName is not None:
            print(f"Welcome {uName}!\n")
            temp = input("Would you like to edit your Guest Controls? (Y/N)")
            if temp == "Y":
                guestControls(uName)
        # Privacy Policy is listed
        print("Privacy Policy: ")
        print("InCollege is committed to protecting your personal information. This Privacy Policy outlines how we collect, handle, and share personal information collected from you while using our website InCollege.")
        print("We Gather Data. We may collect personal information, such as your name, email address, and phone number, as well as non-personal information, such as your IP address and browsing history, when you visit our Website.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # Cookie Policy
    elif link == 6:
        print("Cookie Policy: ")
        print("On our website, InCollege uses cookies and similar technologies to give a better user experience and to better understand how users use our website. This Cookie Policy defines cookies and how we utilize them.")
        print("What exactly are cookies? When you visit a website, little text files called cookies are placed on your device. Cookies enable a website to identify your device and save information about your preferences or previous actions. Cookies are divided into two types: session cookies, which are temporary and expire when you close your browser, and persistent cookies, which remain on your device until they expire or are erased.")
        print("How We Make Use of Cookies. We use cookies to enhance your experience on our site and to better understand how users interact with it.")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # Brand Policy
    elif link == 7:
        print("Brand Policy: ")
        print("InCollege has built a powerful brand that embodies our core beliefs, mission, and quality. This Brand Policy explains how to use our brand assets, such as our logo, name, and trademarks.")
        print("Use of Our Brand Assets. Our brand assets, such as our logo, name, and trademarks, are precious to us. Only with our permission and in compliance with this Policy do we allow others to utilize our brand assets.")
        print("Use of Logo. Our logo is a recognized trademark with copyright protection. You may only use our logo with our express written permission and in accordance with our requirements.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(m, uName)

    # Languages
    elif link == 8:
        if uName is not None:
            lang = input("Languages: English or Spanish? (E/S)")
            if lang == "E":
                print("Language switched to English")
                # update user json to english
                updateUserInfo(uName, "language", "English")
            elif lang == "S":
                print("Spanish Language not available yet")
                # update user json to spanish
                updateUserInfo(uName, "language", "Spanish")
            # Return to options
            select = int(input("0 - Return to previous screen: "))
            if select == 0:
                selectInCollegeImportant(m, uName)

    # Return to previous screen
    elif link == 9:
        print("Returning to previous screen...")
        if i == 0:
            mainPage()
        else:
            selectOption(uName)

    # Invalid option
    else:
        print("Invalid option... Showing options again...")
        selectInCollegeImportant(m, uName)


def guestControls(uName):
    select = int(input("Which setting would you like to turn off: 1 - InCollege Email, 2 - SMS, "
                       "3 - Targeted Advertising, 9 - Return to previous menu\n"))
    if select == 1:
        updateUserInfo(uName, "inCollegeEmail", "off")
        print("InCollege Email successfully turned off, returning to previous menu...")
    elif select == 2:
        updateUserInfo(uName, "SMS", "off")
        print("SMS successfully turned off, returning to previous menu...")
    elif select == 3:
        updateUserInfo(uName, "targetedAds", "off")
        print("Targeted Advertising successfully turned off, returning to previous menu...")
    elif select == 9:
        print("Returning to previous menu...")
        return
    else:
        print("Invalid option, returning to previous menu...")
        return


def selectGeneral(i,Uname):
    selection = int(input("Please select from the following options:\n1 - SignUp\n""2 - Help Center\n3 - About\n""4 - Press \n5 - Blog\n""6 - Careers\n7 - Developers\n""8 - Return to previous screen\n"))
    m = i

    userName = Uname
    if selection == 1:
        if userName is None:
            userName = signUp()
            select = int(input("0 - Return to previous screen: "))
            if select == 0:
                selectGeneral(m, userName)
        else:
            print("Already Signed In")
            select = int(input("0 - Return to previous screen: "))
            if select == 0:
                selectGeneral(m, userName)
    elif selection == 2:
        print("We're here to help")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 3:
        print("In College: Welcome to In College, the world's largest college student network with many users in many"
              " countries and territories worldwide.")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 4:
        print("In College Pressroom: Stay on top of the latest news, updates, and reports")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 5:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 6:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 7:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(m, userName)
    elif selection == 8:
        selectUsefulLinks(m, userName)
    else:
        print("Not a valid option")
        exit(-1)


# this function lists the (up to) 5 current job listings and offers the option to add more if there is room
def findJob(uName):
    # calls the function to print current jobs
    printJobs()

    # gets the dictionary of jobs and counts how many there are into numJobs
    jobs = getJson("jobs")
    numJobs = len(jobs)

    # if there are 4 or less jobs, it offers the user to add another job
    if numJobs < 5:
        postJob = input("Would you like to post a job? (Y/N) ")
        if postJob == "Y":
            createJob(uName)
        elif postJob == "N":
            pass
        else:
            print("Invalid input")
            findJob(uName)
    else:
        # else, it returns to the list of options
        print("Job list is full! Returning to options...")


# this function creates a new job
def createJob(uName):
    # gets the details for the new job from the user
    title = input("Please enter a title: ")
    description = input("Please enter a description: ")
    employer = input("Please enter an employer name: ")
    location = input("Please enter a location: ")
    salary = float(input("Please enter a salary: "))

    # gets the dictionary of jobs and name from the userName
    # then appends to json file
    jobs = getJson("jobs")
    users = readUsers()
    name = "default"
    for user in users:
        if uName == user["username"]:
            name = user["firstName"] + " " + user["lastName"]
    jobs.append(
        {"title": title, "description": description, "employer": employer, "location": location, "salary": salary,
         "Name": name})
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)

    print("Job created! Returning back to options...")


# this function prints the list of jobs in jobs.json
def printJobs():
    # gets the dictionary of jobs
    jobs = getJson("jobs")

    # for loop iterates through all jobs
    i = 0
    for line in jobs:
        # finds the current job in the dictionary
        jobDesc = jobs[i]

        # prints the current job number
        print(f'Job: {i + 1}\n')

        # prints the information about the job
        print(f'Title: {jobDesc["title"]}')
        print(f'Description: {jobDesc["description"]}')
        print(f'Employer: {jobDesc["employer"]}')
        print(f'Location: {jobDesc["location"]}')
        print(f'Salary: {jobDesc["salary"]}')
        print("\n")

        # iterate counter i
        i += 1


# this function opens the jobs.json file and returns a dictionary of values
# EDIT this function now opens multiple json files a returns a dictionary of values
def getJson(fileName):
    try:
        with open(fileName+".json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def findPeople():
    firstName = input("Please enter the first name: ")
    lastName = input("Please enter the last name: ")

    users = readUsers()

    for user in users:
        if firstName == user["firstName"] and lastName == user["lastName"]:
            print("They are a part of the InCollege system")
            # returns true if a person is found
            return True

    print("They are not yet a part of the InCollege system")
    # returns false if a person is not found
    return False


#skills under construction
def selectSkill(uName):
    skill = int(input("Please select a skill to learn from the list:\n1-Time management\n2-Teamwork\n3-Written communication\n4-Verbal communication\n5-Project management\n6-Return to Options menu\n"))
    if skill == 1:
        print("under construction")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectSkill(uName)
    elif skill == 2:
        print("under construction")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectSkill(uName)
    elif skill == 3:
        print("under construction")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectSkill(uName)
    elif skill == 4:
        print("under construction")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectSkill(uName)
    elif skill == 5:
        print("under construction")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectSkill(uName)
    elif skill == 6:
        selectOption(uName)
    else:
        print("Not a valid option")
        exit(-1)


def selectOption(uName):
    option = int(input("Please select from the following options:\n1 - Find a job/internship\n2 - Find someone you know\n""3 - Learn a new skill\n""4 - Useful Links \n5 - InCollege Important Links \n6 - Check pending friends request\n0 - To Log Out\n"))

    if option == 1:
        findJob(uName)
        selectOption(uName)
    elif option == 2:
        if findPeople():        # if findPeople() returns true, it calls back to main to log in or sign up
            return
        else:
            selectOption(uName) # else, it lists the options again
    elif option == 3:
        selectSkill(uName)
        selectOption(uName)
    elif option == 4:
        selectUsefulLinks(1, uName)
    elif option == 5: # InCollege Important Links
        selectInCollegeImportant(1, uName)
    elif option == 6:
        # Get the list of friend requests for the user
        checkFriendRequests(uName)
    elif option == 0:
        print("User logged out")
        exit(1)
    else:
        print("Not a valid option")
        exit(-1)

def searchUsers():
    lastName = input("Please enter the last name or skip: ")
    university = input("Please enter the University name or skip: ")
    major = input("Please enter the major name or skip: ")

    users = readUsers()
    filteredUsers = []
    for user in users:
        if lastName is not None and user["lastName"] != lastName:
            continue
        if university is not None and user["university"] != university:
            continue
        if major is not None and user["major"] != major:
            continue
        filteredUsers.append(user)
    return filteredUsers

def addFriend(uName, friendUsername):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            user["friends"].append(friendUsername)
    with open("users.json", "w") as f:
        json.dump(users, f)

def checkFriendRequests(uName):
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            if user["friendsRequest"]:
                print("You have pending friend requests:")
                for friendRequest in user["friendsRequest"]:
                    print(friendRequest)
                while True:
                    response = input("Do you want to accept or reject the friend request? (A/R): ").upper()
                    if response == "A":
                        friendName = user["friendsRequest"].pop(0)
                        addFriend(uName, friendName)
                        addFriend(friendName, uName)
                        print(f"{friendName} added as a friend.")
                        break
                    elif response == "R":
                        user["friendsRequest"].pop(0)
                        break
                    else:
                        print("Invalid response.")
                        continue
            else:
                print("You have no pending friend requests.")
                break