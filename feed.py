from authentication import *


def HomeScreen():
    print("Welcome to InCollege!")
    print("Meet Jake, a recent college grad in marketing who found out about InCollege at a career fair.")
    print(
        "After creating his profile, connecting with industry professionals, and joining related groups, Jake received a message from a recruiter on InCollege, who was impressed by his profile and wanted to interview him.")
    print("He aced the interview and got the job on the spot. Jake's success shows the value of using InCollege.")


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


def selectSkill():
    skill = input(
        "Please select a skill to learn from the list:\n1-Time management\n2-Teamwork\n3-Written communication\n4-Verbal communication\n5-Project management\n6-Return to main menu\n")
    if skill == 1:
        print("under construction")
    elif skill == 2:
        print("under construction")
    elif skill == 3:
        print("under construction")
    elif skill == 4:
        print("under construction")
    elif skill == 5:
        print("under construction")
    elif skill == 6:
        # selectOption()
        pass
    else:
        print("Not a valid option")
        exit(-1)


def selectOption(uName):
    option = int(input("Please select from the following options:\n1 - Find a job/internship\n2 - Find someone you know\n""3 - Learn a new skill\n0 - To exit\n"))

    if option == 1:
        findJob(uName)
        selectOption(uName)
    elif option == 2:
        if findPeople():        # if findPeople() returns true, it calls back to main to log in or sign up
            return
        else:
            selectOption(uName) # else, it lists the options again
    elif option == 3:
        selectSkill()
        selectOption(uName)
    elif option == 0:
        return
    else:
        print("Not a valid option")
        exit(-1)
