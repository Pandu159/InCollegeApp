import random
from helper import *
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
    applicants = []
    username = uName    
    jobID = random.randint(1000,9999)

    for user in users:
        if uName == user["username"]:
            name = user["firstName"] + " " + user["lastName"]
    jobs.append(
        {"title": title, "description": description, "employer": employer, "location": location, "salary": salary,
         "Name": name, "username": uName, "applicants": applicants, "jobID": jobID})
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)

    print("Job created! Returning back to options...")

# this function shows all the job titles in jobs.json
def showJobs(uName):
    # gets the dictionary of jobs
    jobs = getJson("jobs")

    # gets number of jobs
    numJobs = len(jobs)

    # breaks if there is no job to show
    if numJobs == 0:
        print("There is no job to show.\n")
        return
        
    #for loop iterates through all jobs
    i = 0
    for line in jobs:
        # finds the current job in the dictionary
        jobDesc = jobs[i]
        applied = False

        # indicates if user has applied to job
        for applicants in jobDesc["applicants"]:
            if uName == applicants:
                applied = True

        if applied == True: 
            # prints the current job number
            print(f'{i + 1}' + " - " + f'Title: {jobDesc["title"]}' + "--- APPLICATION SUBMITTED\n")
 
        else:
            # prints the current job number
            print(f'{i + 1}' + " - " + f'Title: {jobDesc["title"]}' + "\n")

        # iterate counter i
        i += 1
    
    
    selection = int(input("Please select a job from the list: "))
    if selection <= 0:
        print("Invalid input")
        showJobs(uName)
    elif selection > i:
        print("Invalid input")
        showJobs(uName)
    else:
        printJobs(selection, uName)
 

# this function prints the details for a particular job
def printJobs(i, uName):
    # gets the dictionary of jobs
    jobs = getJson("jobs")

    # prints the details of the job
    jobDesc = jobs[i-1]
    jobIdentifier = jobDesc["jobID"]

    # prints the information about the job
    print(f'Title: {jobDesc["title"]}')
    print(f'Description: {jobDesc["description"]}')
    print(f'Employer: {jobDesc["employer"]}')
    print(f'Location: {jobDesc["location"]}')
    print(f'Salary: {jobDesc["salary"]}')
    print("\n")


    # applies for job if user did not post the job or has applied to it
    applied = False
    if jobDesc["username"] != uName:
        for applicants in jobDesc["applicants"]:
            if uName == applicants:
                applied = True
                break

        if applied == False:
            applyJob = input("Do you want to apply for this job? (Y/N) ")
            if applyJob.lower() == "y":
                applyForJob(i, uName)
            elif applyJob.lower() == "n":
                saveJob = input("Do you want to save this job? (Y/N) ")
                if saveJob.lower() == "y":
                    saveJobs(jobIdentifier, uName)
                if applyJob.lower() == "n":
                    pass
            else:
                print("Invalid input")
                printJobs(i, uName)
        else:
            pass

    # deletes the job if user posted the job
    else: 
        selection = input("Do you want to delete this job? (Y/N) ")
        if selection.lower() == "y":
            deleteJob(i, uName)
        elif selection.lower() == "n":
            pass
        else:
            print("Invalid input")
            printJobs(i, uName)

    

# this function lists the (up to) 10 current job listings and offers the option to add more if there is room
def showOptions(uName):

    # selects from job menu
    option = int(input(
        "Please select from the following options:\n1 - Show jobs you already applied to\n2 - Show jobs saved\n3 - Show all jobs\n4 - Post a new job\n5 - Return to main menu\n"))

    if option == 1:
        showAppliedJobs(uName)
      
    elif option == 2:
        showSavedJobs(uName)
      
    elif option == 3:
        showJobs(uName) 

    elif option == 4:
        postJob(uName)  
    
    elif option == 5:
        returnToOption(0, uName)
        
    else: 
        print("Invalid input")
        exit(-1)

# posts a new job
def postJob(uName):
    # gets the dictionary of jobs and counts how many there are into numJobs
    jobs = getJson("jobs")
    numJobs = len(jobs)

    # if there are 9 or less jobs, it offers the user to add another job
    if numJobs < 10:
        postJob = input("Would you like to post a job? (Y/N) ")
        if postJob.lower() == "y":
            createJob(uName)
        elif postJob.lower() == "n":
            pass
        else:
            print("Invalid input")
            
    else:
        # else, it returns to the list of options
        print("Job list is full! Returning to options...")


# this function allows a user to apply for a job
def applyForJob(i, uName):
    # gets the dictionary of jobs and applications
    jobs = getJson("jobs")
    
    # gets the job ID 
    jobSelected = jobs[i-1]
    jobIdentifier = jobSelected["jobID"]

    createApplication(jobIdentifier, uName)

    # adds job to jobsApplied in users
    users = readUsers()
    for user in users:
        if user["username"] == uName:
            user["jobsApplied"].append(jobIdentifier)
    with open("users.json", "w") as f:
        json.dump(users, f)

    # adds username to applicants 
    jobSelected["applicants"].append(uName)
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)

# this function saves the job in the Saved Jobs list for the user
def saveJobs(jobId, uName):
    users = readUsers()
    saved = False
    for user in users:
        if user["username"] == uName:
            for job in user["jobsSaved"]:
                if jobId == job:
                    saved = True
                    break
            
            if saved == False:  
                user["jobsSaved"].append(jobId)
                
            else:
                pass
    with open("users.json", "w") as f:
        json.dump(users, f)

# this functions delete a job ***not finished yet
def deleteJob(i, uName):

    # gets the dictionary of jobs
    jobs = getJson("jobs")    
 
    # gets the job ID   
    jobSelected = jobs[i-1]
    jobIdentifier = jobSelected["jobID"]

    # gets list of the job applicants
    jobApplicants = []
    jobApplicants.append(jobSelected["applicants"])

     
    jobs.remove(jobSelected)
    with open("jobs.json", "w") as f:
        json.dump(jobs, f)
     
    
# adds application to applications.json
def createApplication(jobId, uName):
    # gets the dictionary of applications
    applications = getJson("applications")

    # gets the details for the application
    gradDate = input("Please enter graduation date (mm/dd/yyyy): ")
    startDate = input("Please enter a start date (mm/dd/yyyy): ")
    description = input("Please explain why you would be a good fit for this job: ")

    applications.append(
        {"username": uName, "jobID": jobId, "gradDate": gradDate, "startDate": startDate, "description": description})
    with open("applicantions.json", "w") as f:
        json.dump(applications, f)

    print("Application submitted!")
    return

# shows applied jobs
def showAppliedJobs(uName):
    users = readUsers()

    # gets the dictionary of jobs
    jobs = getJson("jobs")    

    # gets the jobs ID from the appliedJobs list for user
    jobsID = []
    for user in users:
        if user["username"] == uName:
            for job in user["jobsApplied"]:
                jobsID.append(job)

    # show list of applied jobs by the user
    numJobs = len(jobsID)
    if numJobs == 0:
        print("You have not applied to any job yet.\n")
    
    else:
        # find the Title for the jobs
        for job in jobs:
            for jobsIDs in jobsID:
                if job["jobID"] == jobsIDs:
                    print(f'Applied: {job["title"]}' + " - " + f'Employer: {job["employer"]}' + "\n\n")  
            
    return


# shows saved jobs
def showSavedJobs(uName):
    users = readUsers()

    # gets the dictionary of jobs
    jobs = getJson("jobs")    

    # gets the jobs ID from the savedJobs list for user
    jobsID = []
    #savedJobs = []
    for user in users:
        if user["username"] == uName:
            for job in user["jobsSaved"]:
                jobsID.append(job)

    # show list of applied jobs by the user
    numJobs = len(jobsID)
    if numJobs == 0:
        print("You have not saved any job.\n")
    
    else:
        # find the Title for the jobs
        for job in jobs:
            for jobsIDs in jobsID:
                if job["jobID"] == jobsIDs:
                    #savedJobs.append({"jobId": jobsIDS, "title": job["title"], "employer": job["employer"]})
                    print(f'Saved: {job["title"]}' + " - " + f'Employer: {job["employer"]}' + "\n\n")  

    #unsave message option        
            
    return
