from network_utils import *
from helper import *
from job_utils import *
from profiles import *

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
    print(
        "After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.")
    print("He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.")


def selectUsefulLinks(i, uName):
    link = int(input(
        "Please select a skill to learn from the list:\n1-General\n2-Browse InCollege\n3-Business Solutions\n4-Directories\n5-Return to previous screen\n"))

    if link == 1:
        selectGeneral(i, uName)
    elif link == 2:
        print("under construction")
        selectUsefulLinks(i, uName)
    elif link == 3:
        print("under construction")
        selectUsefulLinks(i, uName)
    elif link == 4:
        print("under construction")
        selectUsefulLinks(i, uName)
    elif link == 5:
        if (i == 0):
            mainPage()
        else:
            selectOption(uName)

    else:
        print("Not a valid option")
        exit(-1)


def selectInCollegeImportant(i, uName):
    link = int(input(
        "Please select a link from the following:\n 1 - Copyright Notice\n 2 - About\n 3 - Accessibility\n 4 - User Agreement\n 5 - Privacy Policy\n "
        "6 - Cookie Policy\n 7 - Brand Policy\n 8 - Languages\n 9 - Return to previous screen\n"))

    # Copyright Notice
    if link == 1:
        print("Copyright Notice: Developers of InCollege App")
        print(
            "Copyright © 2023 InCollege. All rights reserved.\nAll materials on this website, including but not limited to text, graphics, logos, images, and software, are the property of InCollege and are protected by copyright laws. InCollege prohibits any reproduction, modification, distribution, transmission, or display of any content on this website without prior written permission.\n")
        print(
            "By using this website, you acknowledge that you have read and understood this copyright notice and agree to abide by its terms and conditions.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # About
    elif link == 2:
        print(
            "About\nIntroducing InCollege, a platform designed specifically for college students to connect and grow their professional networks.\nYou are about to embark on an exciting journey filled with opportunities and challenges. By connecting you with other like-minded individuals, mentors, and employers, we are here to support you every step of the way.\n")
        print(
            "Our platform is designed to help you build your professional network, showcase your skills and experiences, and discover exciting career opportunities whether you're just starting your academic career or nearing graduation.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # Accessibility
    elif link == 3:
        print("Accessibility options")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # User Agreement
    elif link == 4:
        print("User Agreement = yes")
        print(
            "This User Agreement regulates your use of the Company's website and is a legal agreement between you and InCollege. You agree to be bound by this Agreement by accessing or using the Website. ")
        print(
            "Use of the Website. The Company provides you a non-exclusive, non-transferable, revocable license to access and use the Website solely for personal, non-commercial purposes. You agree not to use the Website for any illegal purpose or in any way that could harm, disable, overburden, or impair it.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # Privacy Policy
    elif link == 5:
        # A signed-in user will have the option to edit their Guest Controls
        if uName is not None:
            print(f"Welcome {uName}!\n")
            temp = input("Would you like to edit your Guest Controls? (Y/N)")
            if temp == "Y":
                guestControls(uName)
        # Privacy Policy is listed
        print("Privacy Policy:")
        print(
            "InCollege is committed to protecting your personal information. This Privacy Policy outlines how we collect, handle, and share personal information collected from you while using our website InCollege.")
        print(
            "We Gather Data. We may collect personal information, such as your name, email address, and phone number, as well as non-personal information, such as your IP address and browsing history, when you visit our Website.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # Cookie Policy
    elif link == 6:
        print("Cookie Policy:")
        print(
            "On our website, InCollege uses cookies and similar technologies to give a better user experience and to better understand how users use our website. This Cookie Policy defines cookies and how we utilize them.")
        print(
            "What exactly are cookies? When you visit a website, little text files called cookies are placed on your device. Cookies enable a website to identify your device and save information about your preferences or previous actions. Cookies are divided into two types: session cookies, which are temporary and expire when you close your browser, and persistent cookies, which remain on your device until they expire or are erased.")
        print(
            "How We Make Use of Cookies. We use cookies to enhance your experience on our site and to better understand how users interact with it.")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

    # Brand Policy
    elif link == 7:
        print("Brand Policy: ")
        print(
            "InCollege has built a powerful brand that embodies our core beliefs, mission, and quality. This Brand Policy explains how to use our brand assets, such as our logo, name, and trademarks.")
        print(
            "Use of Our Brand Assets. Our brand assets, such as our logo, name, and trademarks, are precious to us. Only with our permission and in compliance with this Policy do we allow others to utilize our brand assets.")
        print(
            "Use of Logo. Our logo is a recognized trademark with copyright protection. You may only use our logo with our express written permission and in accordance with our requirements.")
        # Return to options
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectInCollegeImportant(i, uName)

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
                selectInCollegeImportant(i, uName)

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
        selectInCollegeImportant(i, uName)


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


def selectGeneral(i, Uname):
    selection = int(input(
        "Please select from the following options:\n1 - SignUp\n""2 - Help Center\n3 - About\n""4 - Press \n5 - Blog\n""6 - Careers\n7 - Developers\n""8 - Return to previous screen\n"))

    userName = Uname
    if selection == 1:
        if userName is None:
            userName = signUp()
            select = int(input("0 - Return to previous screen: "))
            if select == 0:
                selectGeneral(i, userName)
        else:
            print("Already Signed In")
            select = int(input("0 - Return to previous screen: "))
            if select == 0:
                selectGeneral(i, userName)
    elif selection == 2:
        print("We're here to help")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 3:
        print("In College: Welcome to In College, the world's largest college student network with many users in many"
              " countries and territories worldwide.")
        select = int(input("0 - Return to previous screen: "))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 4:
        print("In College Pressroom: Stay on top of the latest news, updates, and reports")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 5:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 6:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 7:
        print("Under construction")
        select = int(input("0 - Return to previous screen\n"))
        if select == 0:
            selectGeneral(i, userName)
    elif selection == 8:
        selectUsefulLinks(i, userName)
    else:
        print("Not a valid option")
        exit(-1)


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


# skills under construction
def selectSkill(uName):
    skill = int(input(
        "Please select a skill to learn from the list:\n1-Time management\n2-Teamwork\n3-Written communication\n4-Verbal communication\n5-Project management\n6-Return to Options menu\n"))
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
    requestDisplay(uName)

    option = int(input(
        "Please select from the following options:\n1 - Find a job/internship\n2 - Find someone you know" +
        "\n""3 - Learn a new skill\n""4 - Useful Links \n5 - InCollege Important Links \n6 - Check pending friends request"+
        "\n7 - Search and add Friends\n8 - Show my network \n9 - Create/Modify Profile \n10 - View my profile \n11 - View friends profiles"
        "\n12 - Check Inbox\n13 - Send Message\n0 - To Log Out\n"
    ))

    if option == 1:
        showOptions(uName)
        selectOption(uName)
    elif option == 2:
        if findPeople():  # if findPeople() returns true, it calls back to main to log in or sign up
            return
        else:
            selectOption(uName)  # else, it lists the options again
    elif option == 3:
        selectSkill(uName)
        selectOption(uName)
    elif option == 4:
        selectUsefulLinks(1, uName)
    elif option == 5:  # InCollege Important Links
        selectInCollegeImportant(1, uName)
    elif option == 6:
        # Get the list of friend requests for the user
        checkFriendRequests(uName)
    elif option == 7:
        searchAndRequest(uName)
    elif option == 8:
        showMyNetwork(uName)
    elif option == 9:
        createProfile(uName)
    elif option == 10:
        viewMyProfile(uName)
    elif option == 11:
        friendsProfile(uName)
    elif option == 12:
        checkInbox(uName)
        selectOption(uName)
    elif option == 13:
        targetUser = input("What user would you like to send a message to?")
        sendMessage(uName, targetUser)
        selectOption(uName)
    elif option == 0:
        print("User logged out")
        exit(1)
    else:
        print("Not a valid option")
        exit(-1)

