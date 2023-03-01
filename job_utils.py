from helper import getJson
from authentication import *


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
