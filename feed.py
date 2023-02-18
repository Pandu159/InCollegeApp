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
    #elif selection == 3:  # InCollegeImportant

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
    jobs = getJobs()
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

    # gets the dictionary of jobs and appends the new job
    jobs = getJobs()
    jobs.append(
        {"title": title, "description": description, "employer": employer, "location": location, "salary": salary,
         "Name": uName})
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)

    print("Job created! Returning back to options...")


# this function prints the list of jobs in jobs.json
def printJobs():
    # gets the dictionary of jobs
    jobs = getJobs()

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

        # increments the counter variable
        i += 1


# this function opens the jobs.json file and returns a dictionary of values
def getJobs():
    try:
        with open("jobs.json", "r") as f:
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
    option = int(input("Please select from the following options:\n1 - Find a job/internship\n2 - Find someone you know\n""3 - Learn a new skill\n""4 - Useful Links \n5 - InCollege Important Links\n0 - To Log Out\n"))

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
   #elif option == 5: # InCollege Important Links

    elif option == 0:
        print("User logged out")
        exit(1)
    else:
        print("Not a valid option")
        exit(-1)
